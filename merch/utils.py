import json
from . models import *

def cookieCart(req):
    #get cookie data, if no cookie , create it
    try:
        cart = json.loads(req.COOKIES['cart'])
        # print(cart)
    except:
        cart = {}
    # print("Cart: ", cart)
    items = []
    order = {'get_cart_total':0, 'get_cart_items':0,'shipping':False}
    cartItems = order['get_cart_items']
    
    for i in cart:
        try:
            cartItems += cart[i]['quantity']
            product = Merch.objects.get(id=i)
            size_id = cart[i]['size_id']
            
            sizes = ProductSize.objects.get(id=size_id)
            size = sizes.__dict__['sizes']
            total = (product.price * cart[i]['quantity'])
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']
            print("<<--CARTDATA-->>: ")
            print(product.price)
            item = {
                'product': {
                    'id': product.id,
                    'title': product.title,
                    'price': product.price,
                    'imgURL': product.image_1,
                },
                'quantity': cart[i]['quantity'],
                'size': size,
                'get_total': total
            }
            items.append(item)
            print("FUCK--->>:",item['product'])

            order['shipping'] = True
        except:
            pass
        print("ITEMS------->>:",items)
    return {
        'cartItems': cartItems,
        'order': order,
        'items': items
    }

def cartData(req):
    cookieData = cookieCart(req)
    print("------->>",cookieData)
    cartItems = cookieData['cartItems']
    order = cookieData['order']
    items = cookieData['items']
    return {
        'cartItems': cartItems,
        'order': order,
        'items': items
    }

def CustomerOrder(request,data):
    #print('Cookies', request.COOKIES)
    #FOR ANONYMOUS USERS
    #get user info and cookie data
    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    #print("ITEMS::::",cookieData['items'])
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(
        email=email,
    )
    customer.name = name
    #save the customer for future
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False
    )
    for item in items:
        print(item)
        product = Merch.objects.get(id=item['product']['id'])
        #print("PRODUCT::::::", product)
        orderItem = OrderItem.objects.create(
            product=product,
            item=item,
            order=order
        )

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode']
        )
    return customer, order
