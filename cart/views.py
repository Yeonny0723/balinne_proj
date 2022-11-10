from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render, redirect
from .models import Cart, CartItem
from shop.models import Product
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from order.forms import OrderForm
from customaccount.models import Address
from django.conf import settings
# Create your views here.


@login_required(login_url='account_login')
def cart(req, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0

        cart_items = CartItem.objects.filter(user=req.user, product__is_active=True)

        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

        tax = total * 0
        grand_total= total + tax

    except ObjectDoesNotExist:
        pass

    currency = settings.CURRENCY

    context = {
        'total':total,
        'tax':tax,
        'grand_total':grand_total,
        'quantity':quantity,
        'cart_items':cart_items,
        'currency':currency,
    }
    
    return render(req, 'cart/cart.html', context)


@login_required(login_url='account_login')
def add_cart(req, product_id):
    current_user = req.user
    product = Product.objects.get(id = product_id, is_active=True)
    appended_qty = 1

    if 'product-qty' in req.POST:
        appended_qty = int(req.POST['product-qty'])

    try: # if user has cart
        cart = Cart.objects.get(user=current_user)
        is_cart_item_exists = CartItem.objects.filter(product=product, user=current_user, cart=cart).exists()
        if is_cart_item_exists:
            old_cart_item = CartItem.objects.get(product=product, user=current_user, cart=cart)
            old_cart_item.quantity += appended_qty
            old_cart_item.save()
        else:
            new_cart_item = CartItem.objects.create(product=product, quantity = appended_qty, user=current_user, cart=cart)
            new_cart_item.save()

    except: # if don't have
        cart = Cart.objects.create(user=current_user)
        new_cart_item = CartItem.objects.create(product=product, quantity = appended_qty, user=current_user)
        new_cart_item.cart = cart
        new_cart_item.save()

    return redirect('cart')


@login_required(login_url='account_login')
def decrement_cart(req, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)
    try: 
        current_user = req.user
        cart_item = CartItem.objects.get(user=current_user, product=product, id=cart_item_id)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('cart')


@login_required(login_url='account_login')
def remove_cart_item(req, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)
    if req.user.is_authenticated:
        cart_item = CartItem.objects.get(user=req.user, product=product, id=cart_item_id)
    else:
        cart = Cart.objects.get(user=req.user)
        cart_item = CartItem.objects.get(cart=cart, product=product, id=cart_item_id)
    
    cart_item.delete() # delete all objects

    return redirect('cart')


@login_required(login_url='account_login')
def checkout(req, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0

        cart_items = CartItem.objects.filter(user=req.user)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = total * 0
        grand_total= total + tax

    except ObjectDoesNotExist:
        pass
    
    form = OrderForm()
    address, address_created = Address.objects.get_or_create(user=req.user)
    address_exists = address.postcode
    if address.postcode:
        address = Address.objects.get(user=req.user)
        form.fields["recipient"].initial = address.recipient
        form.fields["phone_1"].initial = address.phone_1
        form.fields["phone_2"].initial = address.phone_2
        form.fields["email"].initial = address.email
        form.fields["postcode"].initial = address.postcode
        form.fields["doromeong_address"].initial = address.doromeong_address
        form.fields["detail_address"].initial = address.detail_address
        form.fields["extra_address"].initial = address.extra_address
        
    context = {
        'total':total,
        'tax':tax,
        'grand_total':grand_total,
        'quantity':quantity,
        'cart_items':cart_items,
        'form':form,
        'address_exists':address_exists, 
        'address':address,
    }
    
    return render(req, 'cart/checkout.html', context)