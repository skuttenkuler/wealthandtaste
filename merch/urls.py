from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('checkout', views.checkout, name='checkout'),
    path('cart', views.cart, name='cart')
]

