from django import forms

class CouponApplyForm(forms.Form):
	code = forms.CharField(label='Mã giảm giá', max_length=30)