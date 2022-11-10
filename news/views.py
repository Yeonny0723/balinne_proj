from django.shortcuts import render
from .models import News, NewsContent

# Create your views here.
def news(req):
    news = News.objects.all()
    context = {
        'news': news,
    }
    return render(req, 'main/news.html', context)


def news_detail(req, news_id):
    news = News.objects.filter(id=news_id)[0]
    newsContents = NewsContent.objects.filter(news_id=news_id)
    context = {
        'news':news,
        'newsContents':newsContents,
    }
    return render(req, 'main/news_detail.html', context)