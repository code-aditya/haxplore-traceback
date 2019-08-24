from django.urls import path,include
from .views import product_list,product_detail,product_upload
urlpatterns = [
    path('', product_list,name="product-list"),
    path('product/',product_detail,name="product-detail"),
    path('product/upload/',product_upload,name="product-upload"),
] 
