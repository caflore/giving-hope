from django.contrib.auth import models
from django.db.models import fields
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Review

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/reviews.html'
    context_object_name = 'reviews'
    ordering = ['-created']

class UserReviewListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = 'reviews/user_reviews.html'
    context_object_name = 'reviews'
    ordering = ['-created']

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review_detailview.html'
    context_object_name = 'review'

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['title', 'content']
    template_name = 'reviews/review_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['title', 'content']
    template_name = 'reviews/review_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'reviews/review_delete.html'
    context_object_name = 'review'
    success_url = '/reviews'

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False
    
