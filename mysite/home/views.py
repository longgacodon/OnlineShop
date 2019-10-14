from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . forms import RegistrationForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'pages/home.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/login")
    return render(request, 'pages/register.html', {'form': form})