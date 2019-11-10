from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	Name = forms.CharField(label='Username or Email', max_length=30)
	class Meta:
		model = Order
		fields = ['name', 'email', 'address', 'postal_code', 'city']