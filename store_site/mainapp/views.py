from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def index(request):
    title = 'Магазин'
    context = {
        'title': title,
    }
    print(request.resolver_match.url_name)
    return render(request, 'mainapp/index.html', context)


def contact(request):
    title = 'Контакты'
    context = {
        'title': title,
    }
    print(context)
    return render(request, 'mainapp/contact.html', context)


def product(request):
    title = 'Каталог'
    links_menu = ProductCategory.objects.all()
    related_products = Product.objects.all()[:3]
    context = {
        'title': title,
        'links_menu': links_menu,
        'related_products': related_products,
    }
    return render(request, 'mainapp/products.html', context)
