"""giving_hope URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from .apps.comment_review import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('giving_hope.apps.core.urls')),
    path('payment/', include('giving_hope.apps.payment.urls')),
    path('pickup/', include('giving_hope.apps.pickup.urls')),
    path('dropoff/', include('giving_hope.apps.dropoff.urls')),
    path('comments/', include('giving_hope.apps.comment_review.urls'))
]
