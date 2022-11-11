from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import path
# Register your models here.
from .models import *


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSizeInline]

admin.site.register(Merch, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

