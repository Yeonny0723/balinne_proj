from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

# Create your models here.

class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def total_likes(self):
        return self.likes.count()
