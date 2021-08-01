from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('product', views.product, name='product'),
    path('product/category/<int:pk>/', views.product, name='category'),
    path('auth/', include('authapp.urls', namespace='auth'), name='auth'),
    path('basket/', include('basketapp.urls', namespace='basket'), name='basket'),
]
