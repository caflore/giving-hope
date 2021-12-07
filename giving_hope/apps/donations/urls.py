from django.urls import path
from django.contrib.auth import views as auth_views
from giving_hope.apps.donations import views

urlpatterns = [
    path('drop-off/', views.dropoff, name='donations-dropoff'),
    path('pick-up/', views.pickup, name='donations-pickup'),
    path('payment/', views.donate, name='donations-payment')
]
