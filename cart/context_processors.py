from .models import Cart, CartItem
from django.contrib.auth.models import AnonymousUser


def cart_counter(req):
    if 'admin' in req.path:
        return {}
    else:
        cart_count = 0
        if not req.user.is_anonymous:
            try:
                cart_items = CartItem.objects.filter(user=req.user, product__is_active=True)
                for cart_item in cart_items:
                    cart_count += cart_item.quantity
                    
            except (Cart.DoesNotExist, AttributeError):
                req.user = AnonymousUser()
                pass
            return dict(cart_count=cart_count)
        else:
            return dict(cart_count=cart_count)


def newarrival_visited(req):
    if 'admin' in req.path:
        return {}
    else:
        visited_newarrival = False
        try: # handle a case when session variable does not exists
            if req.session['visited_newarrival']:
                return dict(visited_newarrival=True)
            else:
                return dict(visited_newarrival=False)
        except:
            req.session['visited_newarrival'] = False
            return dict(visited_newarrival=False)