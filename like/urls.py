from django.urls import path
from . import views

urlpatterns = [
    path('', views.like_button, name='like_button'),
    path('my_likes/', views.my_likes, name='my_likes'),
]
