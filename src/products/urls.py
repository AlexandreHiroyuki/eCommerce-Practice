# from importlib.resources import path
from django.urls import path

from .views import product_list_view, product_detail_slug_view

urlpatterns = [
    path('', product_list_view, name='products'),
    path('<slug:slug>/', product_detail_slug_view, name='products_details'),
]
