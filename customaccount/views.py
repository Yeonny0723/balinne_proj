# from allauth.socialaccount.models import SocialAccount

# def process_data_naver(req):
#     extra = SocialAccount.objects.get(user=req.user).extra_data
#     context = {
#         'age' : extra.get('age'), # 20-29
#         'gender' : extra.get('gender'), # F
#         'email' : extra.get('email'),
#         'mobile' : extra.get('mobile'),
#         'name' : extra.get('name'),
#         'birthday' : extra.get('birthday'),
#     }
    
#     print(context)

from ast import excepthandler
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from order.models import Order, ProductInOrder, Payment
from customaccount.models import Address
from customaccount.forms import UserForm, AddressForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings


@login_required(login_url='account_login')
def dashboard(req):
    orders = Order.objects.order_by('-created_at').filter(user_id=req.user.id)
    address_exist = Address.objects.filter(user=req.user).exists()
    if address_exist:
        address = Address.objects.get(user=req.user)
    else:
        address = Address.objects.create(user=req.user)

    orders_count = orders.count()
    context = {
        'orders_count': orders_count, 
    }
    return render(req, 'account/dashboard.html', context)


@login_required(login_url='account_login')
def my_orders(req):
    orders = Order.objects.filter(user=req.user).order_by('-created_at') # hypiene:= descending order
    currency = settings.CURRENCY
    context = {
        'orders': orders,
        'currency': currency,
    }
    return render(req, 'account/my_orders.html', context)



@login_required(login_url='account_login')
def edit_profile(req):
    address = Address.objects.get_or_create(user=req.user)[0]

    if req.method == "POST":  
        user_form = UserForm(req.POST, instance=req.user) # we send instance as well because we want to update the previous instance
        address = Address.objects.get_or_create(user=req.user)[0]
        address_form = AddressForm(req.POST, instance=address)
        if user_form.is_valid() and address_form.is_valid():
            user_form.save()
            address_form.save()
            messages.success(req, "Your profile has been updated.")
            return redirect('edit_profile')

    else: # if get request
        user_form = UserForm(instance=req.user)
        address_form = AddressForm(instance=address)
    
        context = {
            'user_form': user_form,
            'address_form': address_form,
        }

        return render(req, 'account/edit_profile.html', context)


@login_required(login_url='account_login')
def order_detail(req, order_id):

    order = Order.objects.get(order_number=order_id)
    ordered_products = ProductInOrder.objects.filter(order__order_number=order_id)
    payment = Payment.objects.get(order=order)
    subtotal = 0
    for item in ordered_products:
        subtotal += item.product_price * item.quantity

    context = {
        'order': order,
        'ordered_products': ordered_products,
        'order_number': order_id, 
        'transID': payment.payment_id, 
        'status': payment.status, 
        'subtotal': subtotal,
    }

    return render(req, "account/order_detail.html", context)


@login_required(login_url='account_login')
def order_refund(req):
    orders = Order.objects.filter(user=req.user).order_by('-created_at') # hypiene:= descending order
    currency = settings.CURRENCY
    context = {
        'orders': orders,
        'currency': currency,
    }
    return render(req, 'account/refund.html', context)


@login_required(login_url='account_login')
def account_resign(req):
    logged_user = req.user
    user_data = User.objects.get(username=logged_user) 
    user_data.delete()
    messages.success(req, "발린느 계정 탈퇴가 완료되었습니다.")
    return redirect('index')