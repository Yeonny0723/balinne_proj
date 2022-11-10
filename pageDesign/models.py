from django.db import models
from django.utils.html import format_html

# Create your models here.
class HomeCarousel(models.Model):
    num = models.IntegerField()
    img = models.ImageField(upload_to='media/pageDesign/')
    img_main_title = models.CharField(max_length=100, null=True, blank=True)
    img_subtitle = models.CharField(max_length=200, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def admin_image(self):
        return format_html('<img src="{0}" style="width: 45px; height:45px;" />'.format(self.img.url))
    
    admin_image.allow_tags = True


class InstaImg(models.Model):
    num = models.IntegerField()
    img = models.ImageField(upload_to='media/pageDesign/instaImg')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def admin_image(self):
        return format_html('<img src="{0}" style="width: 45px; height:45px;" />'.format(self.img.url))
    
    admin_image.allow_tags = True