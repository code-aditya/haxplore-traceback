from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.predictive,name="predictive"),
    path('trending/',views.trending,name="trending"),
]
