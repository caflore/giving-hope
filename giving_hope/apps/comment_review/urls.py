from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.PostList.as_view(), name='comments'),
    path('<slug:slug>/', views.post_detail, name='post_detail')
]
