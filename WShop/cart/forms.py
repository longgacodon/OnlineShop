from django import forms
#from product.models import Product

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range (1, 20)]
#PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range (1, Product.objects.get(id=1).stock)]

class CartAddProductForm(forms.Form):
	quantity = forms.TypedChoiceField(label="Số lượng",
							choices=PRODUCT_QUANTITY_CHOICES,
							coerce=int) #widget=forms.NumberInput
	update = forms.BooleanField(required=False,
							initial=False,
							widget=forms.HiddenInput)