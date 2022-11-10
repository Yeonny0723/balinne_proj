from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.


class CartItemInlines(admin.TabularInline):
    model = CartItem
    extra = 0
    list_display = ('product', 'quantity','user')

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInlines,]
    list_display = ('user', 'id')
    list_display_links = ('user', 'id',)

admin.site.register(Cart,CartAdmin)
