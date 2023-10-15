from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

#This function will get session id
def _cart_id(request):                  # _cart_id is a private function
    cart = request.session.session_key  # geting session_key from browser
    if not cart:
        cart = request.session.create() # if no session create a new session
    return cart

#To increase cart item
def add_cart(request, product_id):
    product = Product.objects.get(id = product_id) #get the product
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart using the cart_id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
            )
    cart.save()        
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1 
        cart_item.save()
    except CartItem().DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    return redirect('cart') 

#To decrease cart item
def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('cart')

def remove_cart_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')
    

def cart(request):
    # current_user = request.user   
    # product = Product.objects.get(name=name) #get the product
    # order = Cart.objects.all()
    
    # return render(request, 'cart.html', {'order':order})
    return render(request, 'cart.html')


# This function will take to cart  
def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        # cart_items = CartItem.objects.filter(cart=cart, is_active = True)
        cart_items = CartItem.objects.filter(cart=cart)

        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
    except ObjectDoesNotExist:
    # except:
        pass
    
    context = {
        'total' : total,
        'quantity' : quantity,
        'cart_items' : cart_items,
        
        # 'amount' : amount,
        
    }
    return render(request, 'cart.html', context)