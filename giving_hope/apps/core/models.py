from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    email_address = models.EmailField(max_length=128)
    message = models.TextField()

    is_resolved = models.BooleanField(default=False)
