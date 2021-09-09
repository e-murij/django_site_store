import random
from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory
from basketapp.models import Basket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    title = 'Магазин'
    context = {
        'title': title,
    }
    return render(request, 'mainapp/index.html', context)


def contact(request):
    title = 'Контакты'
    context = {
        'title': title,
    }
    return render(request, 'mainapp/contact.html', context)


def get_hot_product(products):
    return random.sample(list(products), 1)[0]


def get_related_products(hot_product):
    related_products = Product.objects.select_related('category').filter(is_active=True,
                                                                         category__is_active=True,
                                                                         category=hot_product.category).exclude(
        pk=hot_product.pk)[:3]
    return related_products


def products(request, pk=None, page=1):
    title = 'Каталог'
    links_menu = ProductCategory.objects.filter(is_active=True)
    products = Product.objects.filter(is_active=True, category__is_active=True).order_by('name')
    hot_product = get_hot_product(products)
    related_products = get_related_products(hot_product)
    if pk is not None:
        if pk == 0:
            category = {
                'name': 'все',
                'pk': 0,
            }
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(is_active=True, category__is_active=True,
                                              category__pk=pk).order_by('name')
        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)
        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'related_products': related_products,
            'products': products_paginator,
            'hot_product': hot_product,
        }
        return render(request, 'mainapp/products.html', context)
    context = {
        'title': title,
        'links_menu': links_menu,
        'related_products': related_products,
        'products': products,
        'hot_product': hot_product,
    }
    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    title = 'продукты'
    links_menu = ProductCategory.objects.filter(is_active=True)
    product = get_object_or_404(Product, pk=pk)
    related_products = get_related_products(product)
    context = {
        'title': title,
        'links_menu': links_menu,
        'related_products': related_products,
        'product': product,
    }
    return render(request, 'mainapp/product.html', context)
