from django import forms
from django.forms import ModelForm
# from .models import Promise
from giving_hope.apps.pickup.models import EModel


class DateInput(forms.DateInput):
    input_type = 'date'
    

class EForm(forms.ModelForm):
    class Meta:
        model = EModel
        fields = fields = '__all__'
        widgets = {'date': forms.DateInput(attrs={'class': 'datepicker'})}
       

# class PromiseForm(ModelForm):

#     class Meta:
#         model = Promise
#         fields = fields = '__all__'
#         widgets = {'dob': forms.DateInput(attrs={'type':'date'}),}



        