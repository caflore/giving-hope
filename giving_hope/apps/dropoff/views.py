from django.contrib.auth import views
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client 

#from .models import detail



def home_view(request):
    if request.method == 'POST' :
       
       # Detail = detail()
        name = request.POST.get('emailname')
        toemail =request.POST.get('emailto')
        addr1 =request.POST.get('result1') 
        addr2 =request.POST.get('result2') 
        addr3 =request.POST.get('result3') 
        subject ='Giving Hope - Drop Off Location'
        message ='Thank you for expressing your interest in donation, we look forward to see you soon at the below mentioned address'
        namep = request.POST.get('phonename')
        totext =request.POST.get('phone')
        #Detail.email=toemail
        #Detail.save()

        if toemail != "" :

            data = {
                    'name': name,
                    'email': toemail,
                    'subject':subject,
                    'message':message,
                    'addr1': addr1, 
                    'addr2': addr2,
                    'addr3': addr3
                }
            message ='''
            \n Hello {},

                {}

                {}
                {}
                {}

                \n Thank You.
                \n -Team GivingHope
            '''.format(data['name'], data['message'],data['addr1'],data['addr2'],data['addr3'])
            
            send_mail(data['subject'],message,'',[data['email']],fail_silently=True)

        if totext != "" :

            data = {
                    'namep': namep,
                    'totext': totext,
                    'message':message,
                    'addr1': addr1, 
                    'addr2': addr2,
                    'addr3': addr3
                }
            sendtext ='''
            \n Hello {},

                {}

                \n{}
                \n{}
                \n{}

                \n Thank You.
                \n -Team GivingHope
            '''.format(data['namep'], data['message'],data['addr1'],data['addr2'],data['addr3'])
            account_sid = 'ACd9e1ce1b8b97fab787339eb61c4ac961' 
            auth_token = settings.TWI_AUTH
            client = Client(account_sid, auth_token) 
        
            message = client.messages.create(   
                                    body=sendtext ,  
                                    from_='+18705444104',
                                    to= data['totext']
                                ) 
        
            print(message.sid)

    return render(request, 'dropoff/home.html')


def about(request):
    return render(request, 'dropoff/about.html', {'title': 'About'})

