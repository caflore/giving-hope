from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .forms import UserRegistrationForm, ContactMessageForm

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Message submitted successfully!')
            return redirect('contact')
    else:
        form = ContactMessageForm()
    return render(request, 'core/contact.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'core/profile.html')

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('core-login')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/signup.html', {'form': form})

def login(request):
    return render(request, 'core/login.html')
