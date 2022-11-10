from django.db import models
from category.models import Category
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

# Product related
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    ingredients = models.TextField(max_length=500, blank=True)
    short_desc = models.TextField(max_length=500, blank=True)
    med_desc = models.TextField(max_length=500, blank=True)
    price = models.FloatField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True)
    product_thumbnail_img = models.ImageField(upload_to='shop/productMain_img', max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('product_detail', args = [self.category.slug, self.slug]) # self.category.slug := slug of category of Product


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    gallery_image = models.ImageField(upload_to='shop/productGallery_img', max_length=255)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'productgallery' # dont know
        verbose_name_plural = 'product gallery' # to prevent typo!


class ProductDesc(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    desc_text = models.TextField(blank=True, null=True)
    desc_image = models.ImageField(upload_to='shop/productDesc_img', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.product.product_name


#  New arrival
class NewArrival(models.Model):
    num = models.IntegerField(unique=True)
    month = models.CharField(max_length=50)
    year = models.IntegerField()
    short_preview_desc = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return self.product.product_name


class NewArrivalContent(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    desc_text = models.TextField(blank=True, null=True)
    desc_img = models.ImageField(upload_to='shop/new_arrival_images', max_length=255, blank=True, null=True)
    def __str__(self):
        return self.product.product_name


