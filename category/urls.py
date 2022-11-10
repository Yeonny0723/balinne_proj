from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_view, name='category_view'),
    path('<slug:category_slug>/', views.category_view_detail, name='category_view_detail'),
] 

