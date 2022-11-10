from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, ProductDesc, ProductGallery
from category.models import Category
from like.models import Like

# Create your views here.
def shop(req):
    category = req.GET.get('category',False)
    categories = Category.objects.filter(is_active=True)
    products = Product.objects.filter(category__slug=category, is_active=True)
    if not category: # all product
        products = Product.objects.filter(is_active=True)

    is_empty = False
    if len(products) == 0:
        is_empty = True

    liked_prd_id_lst = []
    if not req.user.is_anonymous:
        user_likes = Like.objects.filter(user=req.user)
        liked_prd_id_lst = [i.product.id for i in user_likes]
    
    context = {
        'categories': categories, 
        'products': products,
        'is_empty': is_empty,
        'liked_prd_id_lst': liked_prd_id_lst, 
    }
    return render(req, 'shop/shop.html', context)


def product_detail(req, category_slug, product_slug):
    product = Product.objects.filter(slug=product_slug, is_active=True)[0]
    productGallery = ProductGallery.objects.filter(product=product)
    prodctDesc = ProductDesc.objects.filter(product=product)

    context = {
        'product':product,
        'productGallery':productGallery,
        'prodctDesc':prodctDesc,
    }
    return render(req, 'shop/product_detail.html', context)