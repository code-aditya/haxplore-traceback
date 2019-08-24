from django.shortcuts import render

# Create your views here.

def product_list(request):
    template_name = 'product_list.html'
    return render(request,template_name)

def product_detail(request):
    template_name = 'product_detail.html'
    return render(request, template_name)

def product_upload(request):
    template_name = 'prodcut_upload.html'
    return render(request,template_name)