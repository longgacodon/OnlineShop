from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm

# Create your views here.
def index(request):
    return render(request, 'pages/home.html')

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request, username=cd['username'],
										password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('Xác nhận thành công')
				else:
					return HttpResponse('Tài khoản đã bị khoá')
			else:
				return HttpResponse('Đăng nhập không hợp lệ')
	else:
		form = LoginForm()
	return render(request, 'pages/login.html', {'form': form})

def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			Profile.objects.create(user=new_user)
			return render(request, 'account/register_done.html', {'new_user': new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request, 'pages/register.html', {'user_form': user_form})

@login_required
def account(request):
	return render(request, 'pages/account.html', {'section': 'account'})

@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Cập nhật thành công.')
		else:
			messages.error(request, 'Lỗi cập nhật.')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)

	return render(request, 'pages/account.html', {'user_form': user_form, 'profile_form': profile_form})