from django.db import models

# Create your models here.
class Donations(models.Model):
    name = models.CharField(max_length=100)
    donate = models.IntegerField(default=0) #stripe stores as cents
    
    def __str__(self):
        return self.name