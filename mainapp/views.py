from django.shortcuts import render


def index(request):
    content = {'title': 'Главная'}
    return render(request, 'mainapp/index.html', content)


def products(request):
    content = {'title': 'Каталог'}
    return render(request, 'mainapp/products.html', content)