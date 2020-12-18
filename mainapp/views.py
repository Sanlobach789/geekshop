from django.shortcuts import render
from .models import ProductCategory, Product


def index(request):
    content = {'title': 'Главная'}
    return render(request, 'mainapp/index.html', content)


def products(request):

    title = 'Каталог'
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    content = {'title': title, 'products': products, 'categories': categories}
    return render(request, 'mainapp/products.html', content)