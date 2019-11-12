from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.contrib.auth.models import User
from .models import Profile
import re #regular expression

class LoginForm(forms.Form):
    username = forms.CharField(label='Tên tài khoản hoặc email', max_length=30)
    password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Xác nhận MK', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')      

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản không được có ký tự đặc biệt.")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tên tài khoản đã tồn tại.")
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Xác nhận mật khẩu không khớp.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')