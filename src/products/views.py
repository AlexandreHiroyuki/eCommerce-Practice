from gc import get_objects
from urllib.request import Request
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Product


def product_featured_list_view(request):
    queryset = Product.objects.featured()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/list.html', context)


def product_featured_detail_view(request, pk=None):
    instance = Product.objects.featured().filter(pk=pk)
    if instance.count() == 1:
        instance = instance.first()
    if instance is None:
        raise Http404('Product does not exists')

    print(instance)
    context = {
        'object': instance
    }
    return render(request, 'products/featured-detail.html', context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/list.html', context)


def product_detail_slug_view(request, slug=None):
    try:
        instance = Product.objects.get(slug=slug, active=True)
    except Product.DoesNotExist:
        raise Http404('Product does not exists.')
    context = {
        'object': instance
    }
    return render(request, 'products/detail.html', context)


def product_detail_view(request, pk=None, *args, **kwargs):
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404('Product does not exists.')

    context = {
        'object': instance
    }
    return render(request, 'products/detail.html', context)
