from django.shortcuts import render, redirect
from core import forms
from django.contrib.auth import login, logout, decorators

def homepage(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        f = forms.UserAuthenticateForm(request.POST)
        if f.is_valid():
            login(request, f.cleaned_data['user'])
            return redirect('community-home')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('homepage')


def equipments_list(request):
    return render(request, 'product_list.html')


def equipment_new(request):
    return render(request, 'equipment_upload.html')
