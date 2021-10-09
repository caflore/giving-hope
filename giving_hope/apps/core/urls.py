from django.urls import path
from giving_hope.apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
]
