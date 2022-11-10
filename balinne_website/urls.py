"""balinne_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

# error handler
from django.conf.urls import handler400, handler404, handler500

urlpatterns = [
    # admin
    path('admin-balinne-admin-keepItConfidential/', admin.site.urls),
    # security
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    # multi language setting
    path('i18n/', include('django.conf.urls.i18n')),
    # set currency
    path('set_currency/', views.set_currency, name='set_currency'),
    # main
    path('', views.index, name='index'),
    path('home/', views.to_home, name='to_home'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    # account
    path('accounts/', include('allauth.urls')),
    path('accounts/join/', TemplateView.as_view(template_name='account/join.html'),name='account_join'),
    # shop
    path('shop/', include('shop.urls')),
    # category
    path('category/', include('category.urls')),
    # order
    path('order/', include('order.urls')),
    # cart
    path('cart/', include('cart.urls')),
    # dashboard
    path('dashboard/', include('customaccount.urls')),
    # newArrival
    path('newArrival/', views.newArrival, name='newArrival'),
    # like
    path('like/', include('like.urls')),
    # legal notice
    path('terms-and-conditions/', views.termsNConditions, name='termsNConditions'),
    path('privacy-policy/', views.privacyPolicy, name='privacyPolicy'),
    path('refund-policy/', views.refundPolicy, name='refundPolicy'),
    # news
    path('news/', include('news.urls')),
    # visit
    path('visit/', views.visit, name='visit'),
    # contact
    path('contact/', views.contact, name='contact'),
    # media & static loading on debug false
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


handler400 = 'balinne_website.views.bad_request'
handler404 = 'balinne_website.views.page_not_found'
handler500 = 'balinne_website.views.server_error'