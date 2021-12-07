from django.db import models
from django.db.models.fields import EmailField
from django.utils.translation import ugettext as _

from localflavor.us.models import USStateField, USZipCodeField
from phonenumber_field.modelfields import PhoneNumberField

class DonationPickUp(models.Model):
    first_name = models.CharField(max_length=128)
    lasts_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phone = PhoneNumberField()

    address_1 = models.CharField(_("address"), max_length=128)
    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)
    city = models.CharField(_("city"), max_length=64)
    state = USStateField(_("state"))
    zip_code = models.CharField(_("zip code"), max_length=5)

    is_complete = models.BooleanField(default=False)
