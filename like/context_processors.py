from django.contrib.auth.decorators import login_required
from like.models import Like


def like_counter(req):
    if 'admin' in req.path:
        return {}
    else:
        likes_count = 0
        if req.user.is_anonymous:
            return dict(likes_count=likes_count)
        else:
            likes_count = len(Like.objects.filter(user=req.user))
            return dict(likes_count=likes_count)