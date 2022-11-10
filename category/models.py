from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    num = models.IntegerField()
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

    def get_url(self):
        return reverse('category_view_detail', args=[self.slug]) 


class Collection(models.Model):
    short_desc = models.TextField(max_length=255, blank=True)
    collection_thumbnail = models.ImageField(upload_to='collection/thumbnail',blank=True)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.category.category_name

    def get_url(self):
        return reverse('products_by_category', args=[self.slug]) 
