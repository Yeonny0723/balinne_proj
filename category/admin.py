from django.db import models
from django.contrib import admin
from .models import Category, Collection
from balinne_website.admin import AdminImageWidget

# Register your models here.

class CollectionInlines(admin.TabularInline):
    model = Collection
    extra = 1
    # turn images in admin page visible
    formfield_overrides = { 
        models.ImageField: {'widget': AdminImageWidget}
    }

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    inlines = [CollectionInlines,]
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('num','category_name','is_active',)
    list_display_links = ('num', 'category_name')
    admin_order_field = 'num'

admin.site.register(Category, CategoryAdmin)
