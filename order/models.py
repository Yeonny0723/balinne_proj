from django.db import models
from django.db import models
from django.contrib.auth.models import User
from customaccount.models import Address
from shop.models import Product

# Create your models here.
class Order(models.Model):
    STATUS = (
        ('Ordered','Ordered'),
        ('Paid', 'Paid'),
        ('Cancelled', 'Cancelled'),
    )
    order_status = (
        ('입금확인중','입금확인중'),
        ('결제완료','결제완료'),
        ('상품준비중','상품준비중'),
        ('발송완료','발송완료'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # address
    recipient = models.CharField(max_length=50, null=False)
    phone_1 = models.CharField(max_length=50, null=False)
    phone_2 = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True)
    postcode = models.CharField(max_length=50, null=False)
    doromeong_address = models.CharField(max_length=200,null=False)
    detail_address = models.CharField(max_length=200)
    extra_address = models.CharField(max_length=200)
    to_save = models.BooleanField(default=False)

    # about Order
    order_number = models.CharField(max_length=20)
    order_note = models.CharField(max_length=300, blank=True, null=True)
    order_total = models.FloatField()
    tax = models.FloatField()
    tracking_number = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    order_status = models.CharField(max_length=10, choices=order_status, default='입금확인중')
    ip = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # will process on
    time_range = models.CharField(max_length=20)

    def full_address(self):
        return f'{self.postcode} {self.doromeong_address} {self.extra_address} {self.detail_address} '

    def set_time_range(self, time_border=6):
        t = self.created_at.hour
        if t <= time_border:
            self.time_range =  'Morning'
        else:
            self.time_range =  'Afternoon'
        return self.user.username

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product_price = models.FloatField()
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name

