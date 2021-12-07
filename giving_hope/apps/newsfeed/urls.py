from django.urls import path
from django.contrib.auth import views as auth_views

from giving_hope.apps.newsfeed import views

urlpatterns = [
    path('', views.newsfeed, name='newsfeed'),
    path('orgs', views.organizations, name='orgs'),
]
