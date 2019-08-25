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

def register(request):
    template_name = 'register.html'
    if request.method == 'POST':
        post = request.POST
        data=dict(
            name=post['name'], email=post['email'], password=post['password'],user=request.user.id
        )
        data['language']=post['language']
        data['state']=post['farmer_state']
        data['district']=post['farmer_district']
        data['land_area']=post['land_area']
        data['contact']=post['farmer_contact']
        form = forms.FarmerRegistrationForm(data)
        if form.is_valid():
            form.save()
    return render(request,template_name)

def user_logout(request):
    logout(request)
    return redirect('homepage')


