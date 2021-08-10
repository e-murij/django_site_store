from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from authapp.models import ShopUser
from django.urls import reverse, reverse_lazy
from authapp.forms import ShopUserRegisterForm
from mainapp.models import ProductCategory, Product
from authapp.forms import ShopUserEditForm
from adminapp.forms import CategoryEditForm
from adminapp.forms import ProductEditForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'админ. панель/ пользователи'
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#     context = {
#         'title': title,
#         'users': users_list,
#     }
#     return render(request, 'adminapp/users.html', context)

class UserListView(LoginRequiredMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    context_object_name = 'users'
    def get_queryset(self):
        return ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    def get_context_data(self):
        context = super(UserListView, self).get_context_data()
        title = 'админка/пользователи'
        context.update({'title': title})
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def user_create(request):
#     title = 'пользователи/создать'
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:users'))
#     else:
#         user_form = ShopUserRegisterForm()
#     context = {
#         'title': title,
#         'form': user_form
#     }
#     return render(request, 'adminapp/user_update.html', context)


class UserCreateView(LoginRequiredMixin, CreateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    form_class = ShopUserRegisterForm
    success_url = reverse_lazy('admin_staff:users')

    def get_context_data(self):
        context = super(UserCreateView, self).get_context_data()
        title = 'пользователи/создать'
        context.update({'title': title})
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def user_update(request, pk):
#     title = 'пользователи/редактирование'
#     edit_user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         edit_form = ShopUserEditForm(request.POST, request.FILES, instance=edit_user)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:user_update', args=[edit_user.pk]))
#     else:
#         edit_form = ShopUserEditForm(instance=edit_user)
#     content = {
#         'title': title,
#         'form': edit_form
#     }
#     return render(request, 'adminapp/user_update.html', content)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin_staff:users')
    form_class = ShopUserEditForm

    def get_context_data(self):
        context = super(UserUpdateView, self).get_context_data()
        title = 'пользователи/редактирование'
        context.update({'title': title})
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def user_delete(request, pk):
#     user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'GET':
#         user.is_active = False if user.is_active else True
#         user.save()
#     return HttpResponseRedirect(reverse('admin_staff:users'))

class UserDeleteView(LoginRequiredMixin,DeleteView):
    model = ShopUser
    success_url = reverse_lazy('admin_staff:users')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False if self.object.is_active else True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def categories(request):
#     title = 'админка/категории'
#     categories_list = ProductCategory.objects.all().order_by('-is_active')
#     content = {
#         'title': title,
#         'categories': categories_list
#     }
#     return render(request, 'adminapp/categories.html', content)


class ProductCategoryListView(LoginRequiredMixin, ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return ProductCategory.objects.all().order_by('-is_active')

    def get_context_data(self):
        context = super(ProductCategoryListView, self).get_context_data()
        title = 'админка/категории'
        context.update({'title': title})
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#     title = 'категории/создание'
#     if request.method == 'POST':
#         user_form = CategoryEditForm(request.POST)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:categories'))
#     else:
#         user_form = CategoryEditForm()
#     content = {'title': title, 'form': user_form}
#     return render(request, 'adminapp/category_update.html', content)


class ProductCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_staff:categories')
    form_class = CategoryEditForm

    def get_context_data(self):
        context = super(ProductCategoryCreateView, self).get_context_data()
        title = 'категории/создание'
        context.update({'title': title})
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#     title = 'категории/редактирование'
#     edit_category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         edit_form = CategoryEditForm(request.POST, instance=edit_category)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:category_update', args=[edit_category.pk]))
#     else:
#         edit_form = CategoryEditForm(instance=edit_category)
#     content = {'title': title, 'update_form': edit_form}
#     return render(request, 'adminapp/category_update.html', content)


class ProductCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_staff:categories')
    form_class = CategoryEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/редактирование'
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#     category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'GET':
#         category.is_active = False if category.is_active else True
#         category.save()
#     return HttpResponseRedirect(reverse('admin_staff:categories'))


class ProductCategoryDeleteView(LoginRequiredMixin,DeleteView):
    model = ProductCategory
    success_url = reverse_lazy('admin_staff:categories')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False if self.object.is_active else True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk, page=1):
    title = 'админка/продукт'
    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('-is_active', 'name')
    paginator = Paginator(products_list, 3)
    try:
        products_list_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_list_paginator = paginator.page(1)
    except EmptyPage:
        products_list_paginator = paginator.page(paginator.num_pages)
    context = {
        'title': title,
        'category': category,
        'products': products_list_paginator,
    }
    return render(request, 'adminapp/products.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    title = 'продукты/создание'
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('adminapp:products', args=[pk]))
    else:
        product_form = ProductEditForm(initial={'category': category})
    context = {
        'title': title,
        'update_form': product_form,
        'category': category,
    }
    return render(request, 'adminapp/product_update.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def product_read(request, pk):
#     title = 'продукты/подробнее'
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'title': title,
#         'product': product,
#     }
#     return render(request, 'adminapp/product_read.html', context)


class ProductDetailView(LoginRequiredMixin,DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'продукты/подробнее'
        return context


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = 'продукты/редактирование'
    edit_product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:product_update', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)
    context = {
        'title': title,
        'update_form': edit_form,
        'category': edit_product.category,
    }
    return render(request, 'adminapp/product_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        product.is_active = False if product.is_active else True
        product.save()
        return HttpResponseRedirect(reverse('adminapp:products', args=[product.category.pk]))
