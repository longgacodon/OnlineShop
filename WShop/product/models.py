from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=200, verbose_name="Tên", db_index=True)
	slug = models.SlugField(max_length=200, verbose_name="URL", unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'Danh mục'
		verbose_name_plural = 'Danh mục'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('product:product_list_by_category', args=[self.slug])

class Product(models.Model):
	category = models.ForeignKey(Category, verbose_name="Danh mục", related_name='products', 
									on_delete=models.CASCADE)
	name = models.CharField(max_length=200, verbose_name="Tên", db_index=True)
	slug = models.SlugField(max_length=200, verbose_name="URL", db_index=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name="Hình ảnh", blank=True)
	description = models.TextField(blank=True, verbose_name="Mô tả 1")
	description2 = models.TextField(blank=True, verbose_name="Mô tả 2")
	price = models.DecimalField(max_digits=16, verbose_name="Giá", decimal_places=0)
	stock = models.PositiveIntegerField(verbose_name="Tồn kho")
	available = models.BooleanField(default=True, verbose_name="Bày bán?")
	created = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
	updated = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")

	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'))
		verbose_name = 'Sản phẩm'
		verbose_name_plural = 'Sản phẩm'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('product:product_detail', args=[self.id, self.slug])

class Review(models.Model):
	product = models.ForeignKey(Product, verbose_name="Sản phẩm", on_delete=models.CASCADE, related_name='reviews')
	name = models.CharField(max_length=80, verbose_name="Họ và tên")
	email = models.EmailField()
	body = models.TextField(verbose_name="Bình luận")
	created = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
	updated = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")
	active = models.BooleanField(default=True, verbose_name="Hiện")

	class Meta:
		verbose_name = 'Đánh giá'
		verbose_name_plural = 'Đánh giá'
		ordering = ('created',)

	def __str__(self):
		return 'Đánh giá bởi {} vào {}'.format(self.name, self.product)