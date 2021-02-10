from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def main(request):
    products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')[:3]
    content = {
        'title': 'GeekShop',
        'products': products
    }
    return render(request, 'mainapp/index.html', content)


def products(request, id=None):

    content = {
        'title': 'GeekShop - Категории',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'mainapp/products.html', content)