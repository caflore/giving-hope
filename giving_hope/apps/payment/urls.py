from django.urls import path
from . import views
from giving_hope.apps.payment import views
#from django.contrib.auth import views

urlpatterns = [
    #path('', views.home_view, name='payment-home'),
    # path('',views.baseview.as_view(), name='home-page'),
     #path('about/', views.about, name='payment-about'),
    path('', views.index, name="index"),
    path('donation/', views.donation, name="donation"),
    path('success/<str:args>/', views.successMsg, name="success"),
   # path('create-checkout-session/',views.CreateCheckoutView.as_view(), name='create-checkout-session'),
   
    
]