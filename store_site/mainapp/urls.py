from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('product', views.products, name='product'),
    path('product/category/<int:pk>/', views.products, name='category'),
    path('product/category/<int:pk>/page/<int:page>/', views.products, name='page'),
    path('product/product/<int:pk>/', views.product, name='product'),
    path('auth/', include('authapp.urls', namespace='auth'), name='auth'),
    path('basket/', include('basketapp.urls', namespace='basket'), name='basket'),
    path('admin_staff/', include('adminapp.urls', namespace='admin_staff'), name='admin_staff'),
    path('orders/', include('ordersapp.urls', namespace='orders'), name='orders'),
    path('', include('social_django.urls', namespace='social')),
]
