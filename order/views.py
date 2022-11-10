from django.shortcuts import render, redirect
from cart.models import Cart, CartItem
from order.models import Order, ProductInOrder, Product, Payment
from customaccount.models import Address
import datetime
from order.forms import OrderForm
from django.contrib import messages

# Create your views here.
def place_order(req, total=0, quantity=0):
    current_user = req.user
    cart_items = CartItem.objects.filter(user=current_user) 
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('shop')
    grand_total = 0

    tax = 0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity

    grand_total = total + tax

    if req.method == 'POST':

        orderForm = OrderForm(req.POST)
        if orderForm.is_valid():
            order = Order()
            order.user = current_user
            order.recipient = orderForm.cleaned_data['recipient']
            order.phone_1 = orderForm.cleaned_data['phone_1']
            order.phone_2 = orderForm.cleaned_data['phone_2']
            order.email = orderForm.cleaned_data['email']
            order.postcode = orderForm.cleaned_data['postcode']
            order.doromeong_address = orderForm.cleaned_data['doromeong_address'] 
            order.detail_address = orderForm.cleaned_data['detail_address']
            order.extra_address = orderForm.cleaned_data['extra_address']
            order.to_save = orderForm.cleaned_data['to_save']
            order.order_note = orderForm.cleaned_data['order_note']
            order.order_total = grand_total
            order.tax = tax
            order.status = 'New'
            order.ip = req.META.get('REMOTE_ADDR')
            order.save()
            current_date = datetime.date.today().strftime("%Y%m%d")
            order_number = current_date + str(order.id)
            order.order_number = order_number
            order.set_time_range()
            order.save()
            
            if 'to_save' in req.POST:
                if 't' in req.POST['to_save'][0]:
                    address, address_created = Address.objects.get_or_create(user=req.user)
                    address.user = current_user
                    address.recipient = orderForm.cleaned_data['recipient']
                    address.phone_1 = orderForm.cleaned_data['phone_1']
                    address.phone_2 = orderForm.cleaned_data['phone_2']
                    address.email = orderForm.cleaned_data['email']
                    address.postcode = orderForm.cleaned_data['postcode']
                    address.doromeong_address = orderForm.cleaned_data['doromeong_address'] 
                    address.detail_address = orderForm.cleaned_data['detail_address']
                    address.extra_address = orderForm.cleaned_data['extra_address']
                    address.save()

            order = Order.objects.get(user=current_user, order_number = order_number)

            context = {
                'order': order, 
                'cart_items': cart_items,
                'total': total,
                'tax': tax, 
                'grand_total':grand_total, 
            }
            return render(req, 'order/payments.html', context)

    else:
        return redirect('checkout', context)


import string
import random
alpha = string.ascii_uppercase
num = string.digits

_order_number = '2022030879'
_payment_id = ''.join(random.choice(alpha + num) for _ in range(5)) #number you want
# payment status : accepted or rejected

def payments(req):
    # body = json.loads(req.body) # send transaction ID & payment method 
    # order = Order.objects.get(user=req.user, is_ordered=False, order_number=body['orderID'])

    order = Order.objects.filter(user=req.user)[0]
   
    # (1) Store transaction details inside Payment model
    payment = Payment()
    payment.user = req.user
    # payment.payment_id = body['transID']
    payment.payment_id = _payment_id
    # payment.payment_method = body['payment_method']
    payment.payment_method = 'naverPay'
    payment.amount_paid = order.order_total
    # payment.status = body['status']
    payment.status = 'paid'
    payment.order = order
    payment.save()

    # (2) updated the order model
    order.payment = payment
    order.status = "Paid" 
    order.order_status = "결제완료"
    order.save()

    # (3) Move the cart items to Order Product table
    cartItems = CartItem.objects.filter(user=req.user)
    for item in cartItems:
        orderProduct = ProductInOrder()
        orderProduct.order_id = order.id
        orderProduct.payment = payment
        orderProduct.user_id = req.user.id
        orderProduct.product_id = item.product_id
        orderProduct.quantity = item.quantity
        orderProduct.product_price = item.product.price
        orderProduct.is_ordered = True
        orderProduct.save() # save method will generate the object's id
        # keep in mind that many to many field (like variaion below) should be assigned after saving an object
        orderproduct = ProductInOrder.objects.get(id=orderProduct.id)
        orderproduct.save()

        # (4) Reduce the quantity of the sold product
        product = Product.objects.get(id=item.product_id, is_active=True)
        product.stock -= item.quantity
        product.save()

    # (5) Clear cart
    cartItems.delete()

    # # (6) Send order receieved email to customer
    # mail_subject = "Thank you for your purchase. "
    # message = render_to_string('orders/order_received_email.html', { # we're going to send html
    #     'user': req.user,
    #     'order': order,
    # }) # email contents
    # to_email = req.user.email # address we're going to send
    # send_email = EmailMessage(mail_subject, message, to=[to_email])
    # send_email.send()
    
    # (7) direct a user to order completed page

    # (8) Send order number & transaction ID back to sendData method via JsonResponse
    data = {
        'order_number': order.order_number, 
        'transID': payment.payment_id,
    }

    # send response back to front end -> then response will be processed to direct a user to payment success view!
    # return JsonResponse(data) # return JsonResponse is to return data back to the front html!! (which is payments.html here)
    return redirect('order_complete')


def order_complete(req):
    # order_number = req.GET.get('order_number')
    # transID = req.GET.get('payment_id')

    print('****transID', _payment_id)
    transID = _payment_id

    try:
        # order = Order.objects.get(order_number=order_number, is_paid=True)
        # order = Order.objects.get(order_number=order_number)
        order = Order.objects.filter(user=req.user).last()
        order_number = order.order_number
        
        ordered_products = ProductInOrder.objects.filter(order_id=order.id)

        subtotal = 0
        for item in ordered_products:
            subtotal += item.product_price * item.quantity

        context = {
            'order': order,
            'ordered_products': ordered_products,
            'order_number': order_number, 
            'transID': transID, 
            'status': '결제완료', 
            'subtotal': subtotal,
        }
        return render(req, 'order/order_complete.html', context)
    
    except Order.DoesNotExist:
        return redirect('index')



def process_refund(req, order_id):
    order = Order.objects.get(order_number = order_id, user=req.user)
    order.status = 'Cancelled'
    order.save()
    messages.success(req, '주문이 성공적으로 취소되었습니다. 영업일 기준 3-5일 결제계좌로 환불됩니다. ') 
    return redirect('order_refund')