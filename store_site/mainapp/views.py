from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory
from basketapp.models import Basket


def index(request):
    title = 'Магазин'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'title': title,
        'basket': basket,
    }
    print(request.resolver_match.url_name)
    return render(request, 'mainapp/index.html', context)


def contact(request):
    title = 'Контакты'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'title': title,
        'basket': basket,
    }
    print(context)
    return render(request, 'mainapp/contact.html', context)


def product(request, pk=None):
    title = 'Каталог'
    links_menu = ProductCategory.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('name')[:3]
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.all().filter(category__pk=pk).order_by('name')[:3]
        context = {
            'title': title,
            'links_menu': links_menu,
            'related_products': products,
            'category': category,
            'products': products,
            'basket': basket,
        }
        return render(request, 'mainapp/products.html', context)


    related_products = Product.objects.all()[:3]
    context = {
        'title': title,
        'links_menu': links_menu,
        'related_products': related_products,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', context)
