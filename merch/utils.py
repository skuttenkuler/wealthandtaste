import json
from . models import *

def cookieCart(req):
    #get cookie data, if no cookie , create it
    try:
        cart = json.loads(req.COOKIES['cart'])
        #print(cart)
    except:
        cart = {}
    print("Cart: ", cart)
    items = []
    order = {'get_cart_total':0, 'get_cart_items':0,'shipping':False}
    cartItems = order['get_cart_items']
    
    for i in cart:
        try:
            cartItems += cart[i]['quantity']
            product = Merch.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']
    
            item = {
                'product': {
                    'id': product.id,
                    'title': product.title,
                    'price': product.price,
                    'imgURL': product.imgURL,
                },
                'quantity': cart[i]['quantity'],
                'get_total': total
            }
            items.append(item)

            order['shipping'] = True
        except:
            pass
    return {
        'cartItems': cartItems,
        'order': order,
        'items': items
    }

def cartData(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(req)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    return {
        'cartItems': cartItems,
        'order': order,
        'items': items
    }