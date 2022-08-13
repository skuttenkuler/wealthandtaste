from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import path
# Register your models here.
from .models import *


#class OrderAdmin(admin.ModelAdmin):
    #info needed name, order items, address
   # list_display = ('customer','date_ordered','transaction_id','complete')

    #def address(self,obj:ShippingAddress) -> str:
      #return f"{str(obj.address)}"


admin.site.register(Merch)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

