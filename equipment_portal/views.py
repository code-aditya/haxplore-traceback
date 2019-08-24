from django.shortcuts import render

# Create your views here.

def product_list(request):
    template_name = 'catalog.html'
    return render(request,template_name)

def product_detail(request):
    template_name = 'community_question.html'
    return render(request, template_name)

def product_upload(request):
    template_name = 'login.html'
    return render(request,template_name)