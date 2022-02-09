from multiprocessing import context
from django.shortcuts import render, get_object_or_404

from .models import Product

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/list.html', context)

def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = Product.objects.get(pk=pk)
    instance = get_object_or_404(Product, pk=pk)
    context = {
        'object': instance
    }
    return render(request, 'products/detail.html', context)