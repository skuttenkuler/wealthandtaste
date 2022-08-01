from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('', views.checkout, name='checkout'),
    path('', views.cart, name='cart')
]

