from django.db import models
from django.db.models.fields import EmailField
from django.utils.translation import ugettext as _

from djmoney.models.fields import MoneyField
from localflavor.us.models import USStateField, USZipCodeField
from phonenumber_field.modelfields import PhoneNumberField

class Organization(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    active_projects = models.IntegerField()
    mission = models.TextField()
    url = models.URLField()
    logo_url = models.URLField()

    def __str__(self) :
        return self.name

class Donation(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    amount = MoneyField(decimal_places=2, default=0, default_currency='USD', max_digits=10)

    transaction_date = models.DateTimeField(auto_now_add=True)

class DonationPickUp(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phone = PhoneNumberField()

    address_1 = models.CharField(_("address"), max_length=128)
    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)
    city = models.CharField(_("city"), max_length=64)
    state = USStateField(_("state"))
    zip_code = models.CharField(_("zip code"), max_length=5)

    pickup_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    pickup_time = models.TimeField(null=True)

    is_complete = models.BooleanField(default=False)
