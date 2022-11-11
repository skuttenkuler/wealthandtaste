from django.db import models
from django.contrib.auth.models import User
import uuid


class Merch(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image_1 = models.CharField(max_length=250,null=True, blank=True)
    image_2 = models.CharField(max_length=250,null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)

    def __str__(self):
        return self.title

    # #image render safe check
    # @property
    # def imgURL(self):
    #     try:
    #         url = self.image_1.url
    #     except:
    #         url = ''
    #     return url

class ProductSize(models.Model):
    CHOICES = (
        ('xs','XS'),
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
        ('xxl', 'XXL')
    )
    sizes = models.CharField(max_length=50, choices=CHOICES, default='l')
    product = models.ForeignKey(Merch, on_delete=models.CASCADE, related_name='sizes')
    quantity = models.IntegerField(default=0)

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.customer) + str(self.transaction_id)
    #calculate cart total
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    #get items in cart
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    #order shipping
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        #validate items in cart
        if orderitems:
            shipping = True
        return shipping 

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
        
class OrderItem(models.Model):
    product = models.ForeignKey(Merch, on_delete=models.SET_NULL, blank=True, null=True)
    size = models.CharField(max_length=50,blank=False, null=False, default='s')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    #get total
    @property
    def get_total(self):
        print("SELF:",self.product.__dict__.values())
        total = self.product.price * self.product.quantity
        return total
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


