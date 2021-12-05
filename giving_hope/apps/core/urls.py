from django.urls import path
from django.contrib.auth import views as auth_views
from giving_hope.apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-up/', views.signup, name='core-signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='core-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='core-logout'),
    path('profile/', views.profile, name='core-profile'),
]
