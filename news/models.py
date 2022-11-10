from django.db import models
import datetime
# Create your models here.

#  New arrival

class News(models.Model):
    # month = models.CharField(max_length=50)
    # year = models.IntegerField()
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True, null=True)
    news_thumbnail = models.ImageField(upload_to='news/thumbnail', max_length=255, blank=True, null=True)
    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
    def date_kr(self):
        year = self.created_at.year
        month = self.created_at.month
        day = self.created_at.day
        return f"{year}.{month}.{day}"


class NewsContent(models.Model):
    desc_text = models.TextField(blank=True, null=True)
    desc_img = models.ImageField(upload_to='news/contents', max_length=255, blank=True, null=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
