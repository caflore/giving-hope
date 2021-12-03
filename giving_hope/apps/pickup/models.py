from django.db import models

# Create your models here.
from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

# class UserProfile(models.Model):
	
# 	updated = models.DateTimeField(auto_now=True)
# 	timestamp = models.DateTimeField(auto_now_add=True)
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	telephone = models.CharField(max_length=15, null=True, blank=True)
	
# 	longitude = models.CharField(verbose_name="Longitude",max_length=50, null=True, blank=True)
# 	latitude = models.CharField(verbose_name="Latitude",max_length=50, null=True, blank=True)
	
# 	is_active = models.BooleanField(default = True)

# 	email_verified = models.BooleanField(default = False)
# 	has_profile = models.BooleanField(default=False)

class contact(models.Model):
    First_name= models.CharField(max_length=100)
    Last_name= models.CharField(max_length=100) 
    email= models.EmailField(max_length=100)
    phone_number= models.IntegerField()
    # address= models.TextField(max_length=200)
    address = models.CharField(verbose_name="Address",max_length=100, null=True, blank=True)
    state = models.CharField(verbose_name="State",max_length=100, null=True, blank=True)
    city = models.CharField(verbose_name="City",max_length=100, null=True, blank=True)
    zip_code = models.CharField(verbose_name="Zip Code",max_length=8, null=True, blank=True)
	# country = models.CharField(verbose_name="Country",max_length=100, null=True, blank=True)
    longitude = models.CharField(verbose_name="Longitude",max_length=50, null=True, blank=True)
    latitude = models.CharField(verbose_name="Latitude",max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default = True)


    def __str__(self):
        return self.First_name



# class YourClassName(models.Model):
#     expiration_date = models.DateField(null=True)

# class Promise(models.Model):
#     dob = models.DateField(verbose_name="Date of birth", blank=True)


class EModel(models.Model):
    date = models.DateField(blank=False)

