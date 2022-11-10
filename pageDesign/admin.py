from django.contrib import admin
from .models import HomeCarousel, InstaImg
import admin_thumbnails

# Register your models here.
@admin_thumbnails.thumbnail('img')
class HomeCarouselAdmin(admin.ModelAdmin):
    list_display = ('num', 'img_main_title', 'admin_image',)
    admin_order_field = 'num'


@admin_thumbnails.thumbnail('img')
class InstaImgAdmin(admin.ModelAdmin):
    list_display = ('num', 'admin_image',)
    admin_order_field = 'num'

admin.site.register(HomeCarousel,HomeCarouselAdmin)
admin.site.register(InstaImg,InstaImgAdmin)
