from django import forms
from product.models import Product

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range (1, 21)]

class CartAddProductForm(forms.Form):
	quantity = forms.TypedChoiceField(label="Số lượng",
							choices=PRODUCT_QUANTITY_CHOICES,
							coerce=int) #widget=forms.NumberInput
	update = forms.BooleanField(required=False,
							initial=False,
							widget=forms.HiddenInput)