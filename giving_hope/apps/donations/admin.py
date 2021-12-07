from django.contrib import admin

from .models import DonationPickUp, Organization, Donation

admin.site.register(DonationPickUp)
admin.site.register(Organization)
admin.site.register(Donation)
