from django.shortcuts import render


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
    links_menu = [
        {'href': 'product', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context)
