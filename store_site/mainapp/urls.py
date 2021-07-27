from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('product', views.product, name='product'),
    path('auth/', include('authapp.urls', namespace='auth'), name='auth'),
]
