from django.contrib import admin
from .models import Product, ProductGallery, ProductDesc, NewArrival, NewArrivalContent
import admin_thumbnails

# Register your models here.

@admin_thumbnails.thumbnail('gallery_image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 0

@admin_thumbnails.thumbnail('desc_image')
class ProductDescInline(admin.TabularInline):
    model = ProductDesc
    extra = 0

class NewArrivalInline(admin.TabularInline):
    model = NewArrival
    extra = 0

class NewArrivalContentInline(admin.TabularInline):
    model = NewArrivalContent
    extra = 0

@admin_thumbnails.thumbnail('product_thumbnail_img')
class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [ProductGalleryInline, ProductDescInline, NewArrivalInline, NewArrivalContentInline, ]
    prepopulated_fields = {'slug':('product_name',)}


class NewArrivalAdmin(admin.ModelAdmin):
    model = NewArrival
    list_display = ('num','product','month','year')
    list_filter = (
        'num',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(NewArrival, NewArrivalAdmin)


