from django.contrib import admin
from .models import Payment, Order, ProductInOrder
from django.contrib.admin import DateFieldListFilter
from rangefilter.filters import DateRangeFilter
import datetime

# Register your models here.

class ProductInOrderInlines(admin.TabularInline):
    model = ProductInOrder
    extra = 0

class PaymentInlines(admin.TabularInline):
    model = Payment
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInOrderInlines,PaymentInlines,]
    # enable to filter by date
    list_filter = (
        ('created_at', DateRangeFilter),
        'time_range',
        'status',
        'order_status'
    )
    search_fields = (
        'order_number', 
        'user__username',
    )
    list_display = ('order_number', 'user', 'created_at','status' ,'order_status')

    def get_rangefilter_created_at_default(self, request):
        return (datetime.date.today, datetime.date.today)

    def get_rangefilter_created_at_title(self, request, field_path):
        return 'Ordered_at'


admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
