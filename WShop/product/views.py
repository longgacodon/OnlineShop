from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from .models import Category, Product, Review
from cart.forms import CartAddProductForm
from .forms import ReviewForm, SearchForm

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'product/list.html', {'category': category,
                    'categories': categories, 'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug,
                                        available=True)

    #Dánh sách các đánh giá
    reviews = product.reviews.filter(active=True)

    new_review = None

    if request.method == 'POST':
        # Đánh giá được tạo
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            # Tạo đánh giá từ form nhưng chưa lưu
            new_review = review_form.save(commit=False)
            # Gán giá trị sản phẩm vào bình luận (Liên kết)
            new_review.product = product
            # Lưu đánh giá vào CSDL
            new_review.save()
    else:
        review_form = ReviewForm()

    cart_product_form = CartAddProductForm()
    return render(request,
                    'product/detail.html', 
                    {'product': product, 'cart_product_form': cart_product_form, 
                    'reviews': reviews, 'new_review': new_review, 'review_form': review_form})

def product_search(request):
    search_form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            search_vector = SearchVector('category', 'name')
            search_query = SearchQuery(query)
            results = Product.objects.annotate(search=search_vector,
                        rank=SearchRank(search_vector, search_query)
                        ).filter(search=search_query).order_by('-rank')

    return render(request, 'product/search.html', {'search_form': search_form, 'query': query, 'results': results})