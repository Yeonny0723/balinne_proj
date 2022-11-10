from django.shortcuts import render
from category.models import Category
from shop.models import Product
from django.contrib import messages

# Create your views here.

def category_view(req):
    categories = Category.objects.filter(is_active=True)
    context = {
        'categories': categories,
    }
    return render(req, 'category/collection.html', context)


def category_view_detail(req, category_slug):
    category = Category.objects.filter(slug=category_slug)[0]
    collection = category.collection
    products = Product.objects.filter(category=category, is_active=True)
    if products:
        context = {
            'collection':collection,
            'products':products,
        }
        return render(req, 'category/category_detail.html', context)
    else:
        messages.success(req, "Sorry, no product is registered yet. ")
        return render(req, 'category/category_detail.html',)