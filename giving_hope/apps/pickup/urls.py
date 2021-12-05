from django.core.exceptions import ViewDoesNotExist
from django.urls import path
from . import views
#from django.contrib.auth import views
from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()
#from dropoff import views

urlpatterns = [
    path('', views.home_view, name='pickup-home'),
    path('about/', views.about, name='pickup-about'),
    path('form/', views.ContactInfo, name='pickup-form'),
    path('thanks/', views.selecttime, name='pickup-thanks'),
    url(r'^datepickerview/$', views.datepickerview)
]


