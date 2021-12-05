from django.urls import path
from . import views
#from django.contrib.auth import views

urlpatterns = [
    path('', views.home_view, name='dropoff-home'),
    path('about/', views.about, name='dropoff-about'),
    
]