from django.contrib import admin
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Address
from cart.models import Cart, CartItem


class CartInline(admin.TabularInline):
    model = Cart
    extra = 0


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0


class SocialAccountInline(admin.TabularInline):
    model = SocialAccount
    extra = 0


class AddressInline(admin.TabularInline):
    model = Address
    extra = 0


class CustomUserAdmin(UserAdmin):
    inlines = [SocialAccountInline, AddressInline, CartInline, CartItemInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Address)

