from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import DonationPickupForm, DonationPaymentForm
from .models import Donation

def dropoff(request):
    return render(request, 'donations/dropoff.html')

def pickup(request):

    if request.method == 'POST':
        form = DonationPickupForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Pick-up scheduled successfully!')
            send_mail(
                'Giving Hope: Pick-Up Scheduled Successfully',
                'Giving Hope appreatiates your kind gesture for a Donation. Giving Hope associate will pickup your donation at your chosen time.',
                settings.EMAIL_HOST_USER,
                [form.data['email']],
            )
            return redirect('donations-pickup')
    else:
        form = DonationPickupForm()

    return render(request, 'donations/pickup.html', {'form': form})

def donate(request):
    if request.method == 'POST':
        form = DonationPaymentForm(request.POST)

        if form.is_valid():
            d = Donation()
            d.first_name = form.cleaned_data['first_name']
            d.last_name = form.cleaned_data['last_name']
            d.email = form.cleaned_data['email']
            d.organization = form.cleaned_data['organization']
            d.amount = form.cleaned_data['amount']
            d.save()

            messages.success(request, f'Thank you for your donation!')
            send_mail(
                'Giving Hope: Donation Successful',
                'Giving Hope appreatiates your kind gesture for a Donation.',
                settings.EMAIL_HOST_USER,
                [form.data['email']],
            )
            return redirect('donations-payment')
    else:
        form = DonationPaymentForm()
    return render(request, 'donations/payment.html', {'form': form})
