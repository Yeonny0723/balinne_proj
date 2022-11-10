from django.shortcuts import render
from .models import Like
from django.shortcuts import get_object_or_404 
import json
from django.http import HttpResponse
from shop.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='account_login')
def like_button(request):
    if request.method =="POST":
        if request.POST.get("operation") == "like_submit" and request.is_ajax():
            current_user = request.user
            product_id=request.POST.get("product_id")
            product = Product.objects.get(id=product_id, is_active=True)

            like = Like()
            try: # if like exists
                like = Like.objects.get(user=current_user, product=product)
                like.delete()
            except: # if not exists
                like.user = current_user
                like.product = product
                like.save()

            ctx={"content_id":product_id}
            return HttpResponse(json.dumps(ctx), content_type='application/json')


@login_required(login_url='account_login')
def my_likes(req):
    likes = Like.objects.filter(user=req.user, product__is_active=True)
    context = {
       'likes':likes, 
    }
    return render(req, 'shop/likes.html', context)