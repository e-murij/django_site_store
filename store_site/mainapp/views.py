from django.shortcuts import render


def index(request):
    title = 'Магазин'
    context = {
        'title': title,
    }
    print(context)
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
    context = {
        'title': title,
    }
    return render(request, 'mainapp/products.html', context)
