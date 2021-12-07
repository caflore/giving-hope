from django.urls import path
from django.contrib.auth import views as auth_views

from giving_hope.apps.reviews import views
from .views import ReviewDetailView, ReviewListView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView, UserReviewListView

urlpatterns = [
    path('', ReviewListView.as_view(), name='reviews'),
    path('your-reviews/', UserReviewListView.as_view(), name='user-reviews'),
    path('new/', ReviewCreateView.as_view(), name='review-create'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('review/<int:pk>/update', ReviewUpdateView.as_view(), name='review-update'),
    path('review/<int:pk>/delete', ReviewDeleteView.as_view(), name='review-delete'),
]
