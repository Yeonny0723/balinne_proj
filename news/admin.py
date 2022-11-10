from django.contrib import admin
from .models import News, NewsContent
import admin_thumbnails
# Register your models here.

@admin_thumbnails.thumbnail('desc_img')
class NewsContentInline(admin.TabularInline):
    model = NewsContent
    extra = 0

@admin_thumbnails.thumbnail('news_thumbnail')
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsContentInline,]
    list_display = ('title','created_at')

admin.site.register(News, NewsAdmin)