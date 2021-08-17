import random
from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory
from basketapp.models import Basket


def index(request):
    title = 'Магазин'
    basket = get_basket(request.user)
    context = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'mainapp/index.html', context)


def contact(request):
    title = 'Контакты'
    basket = get_basket(request.user)
    context = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'mainapp/contact.html', context)


def get_basket(user):
    if user.is_authenticated:
        basket = Basket.objects.filter(user=user)
    else:
        basket = []
    return basket


def get_hot_product():
    product = Product.objects.all()
    return random.sample(list(product), 1)[0]


def get_related_products(hot_product):
    related_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return related_products


def products(request, pk=None):
    title = 'Каталог'
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)
    hot_product = get_hot_product()
    related_products = get_related_products(hot_product)
    products = Product.objects.all().order_by('name')[:3]
    if pk is not None:
        if pk == 0:
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.all().filter(category__pk=pk).order_by('name')[:3]
        context = {
            'title': title,
            'links_menu': links_menu,
            'related_products': related_products,
            'hot_product': hot_product,
            'category': category,
            'products': products,
            'basket': basket,
        }
        return render(request, 'mainapp/products.html', context)
    context = {
        'title': title,
        'links_menu': links_menu,
        'related_products': related_products,
        'hot_product': hot_product,
        'products': products,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    title = 'продукты'
    basket = get_basket(request.user)
    links_menu = ProductCategory.objects.all()
    product = get_object_or_404(Product, pk=pk)
    related_products = get_related_products(product)
    context = {
        'title': title,
        'links_menu': links_menu,
        'related_products': related_products,
        'product': product,
        'basket': basket,
    }
    return render(request, 'mainapp/product.html', context)
