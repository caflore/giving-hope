from django import forms
from django.db.models import fields
from django.forms import widgets
from django.utils.translation import ugettext as _

from djmoney.forms.fields import MoneyField
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField
from localflavor.us.forms import USStateField, USStateSelect, USZipCodeField
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from giving_hope.apps.donations.models import DonationPickUp, Donation, Organization

class DonationPickupForm(forms.ModelForm):
    class Meta:
        model = DonationPickUp
        fields = ['first_name', 'last_name', 'email', 'phone', 'address_1', 'address_2', 'city', 'state', 'zip_code', 'pickup_date', 'pickup_time']
        widgets = {
            'pickup_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'pickup_time': forms.widgets.TimeInput(attrs={'type': 'time'})
        }

class DonationPaymentForm(forms.Form):
    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)
    email = forms.EmailField(max_length=128)
    organization = forms.ModelChoiceField(queryset=Organization.objects.all())
    amount = MoneyField(default_currency='USD')

    address = forms.CharField()
    country = CountryField(blank_label='select country').formfield(widget=CountrySelectWidget(attrs={
        'class': 'custom-select d-block w-100'
    }))
    state = USStateField()
    zip_code = USZipCodeField()

    name_on_card = forms.CharField(max_length=128)
    card_number = CardNumberField(label='Card Number')
    expiration_date = CardExpiryField(label='Expiration Date')
    cvv = SecurityCodeField(label='CVV/CVC')

    class Meta:
        model = Donation
        fields = ['first_name', 'last_name', 'email', 'organization', 'amount']