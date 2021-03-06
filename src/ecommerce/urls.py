"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

# from products.views import (
#     product_list_view,
#     product_detail_view,
#     product_detail_slug_view,
#     product_featured_list_view,
#     product_featured_detail_view
# )

from .views import home_page, contact_page, login_page, register_page


urlpatterns = [
    path('', home_page, name='home'),
    path('contact/', contact_page, name='contact'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('products/', include('products.urls', namespace='products')),
    # path('featured/', product_featured_list_view, name='featured'),
    # path('featured/<int:pk>/', product_featured_detail_view,
    #      name='featured_details'),
    # path('featured/<slug:slug>/', product_featured_detail_view,
    #      name='featured_details'),
    # path('products/', product_list_view, name='products'),
    # path('products/<int:pk>/', product_detail_view, name='products_details'),
    # path('products/<slug:slug>/', product_detail_slug_view, name='products_details'),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
