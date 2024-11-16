# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', category_list_view, name='category_list'),  
    path('categories/<int:pk>/', category_detail_view, name='category_detail'),  

    path('products/', product_list_view, name='product_list'),  
    path('products/<int:pk>/', product_detail_view, name='product_detail'),  

    path('users/', user_list_view, name='user_list'),  
    path('users/<int:pk>/', user_detail_view, name='user_detail'), 
]
