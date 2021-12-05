from django import forms
from django.contrib.auth import views
from django.db.models.fields import CharField
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from django.conf import settings
from django.template import Context, context
#from django.shortcuts import render_to_response

from django.http import HttpResponseRedirect
#from django.core.context_processors import csrf
from django.template import RequestContext
from .forms import EForm

#from blog.forms import DatepickerForm
from .models import contact
from django.http import HttpResponse
# from .forms import PromiseForm
# from .models import Promise


# class PromiseCreateView(CreateView):
#     model = Promise
#     form_class = PromiseForm


def home_view(request):
    
    return render(request, 'pickup/home.html')


def about(request):
    return render(request, 'pickup/about.html', {'title': 'AboutUS'})

# global name1
# global name2
# global email
# global phone_numbers

def ContactInfo(request):
    
    if request.method=="POST" :
        Contact= contact()
        name1=request.POST.get('Fname')
        name2=request.POST.get('Lname')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        addresss=request.POST.get('address')
      

        id_date1=request.POST.get('id_date1')
        rad1=request.POST.get('rad1')
        id_date2=request.POST.get('id_date2')
        rad2=request.POST.get('rad2')
        id_date3=request.POST.get('id_date3')
        rad3=request.POST.get('rad3')
        
       
        Contact.First_name=name1
        Contact.Last_name=name2
        Contact.email=email
        Contact.phone_number=phone_number
        Contact.address=addresss
        Contact.save()

        google_api_key = settings.GOOGLE_API_KEY


        return HttpResponse("thank you for your information")

    #send_mail('pick','picksch','givinghopeproj@gmail.com',['@gmail.com'],fail_silently=True)


    return render(request, 'pickup/form.html')


def selecttime(request):
    

    if request.method == 'POST':
		#amount = int(request.POST['amount'])
		#email=request.POST['email']
		#name=request.POST['nickname']
		#det = (amount,"&",email,"&",name)	
        #name1 = name
        #toemail = eml
        # name1=""
        # toemail="@gmail.com"
        
        name1=request.POST.get('Fname')
        name2=request.POST.get('Lname')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')

        id_date1=request.POST.get('id_date1')
        rad1=request.POST.get('rad1')
        id_date2=request.POST.get('id_date2')
        rad2=request.POST.get('rad2')
        id_date3=request.POST.get('id_date3')
        rad3=request.POST.get('rad3')
        
        subject = 'Giving Hope Donation Pickup Update'
        message = "Giving Hope appreatiates your kind gesture for a Donation. Giving Hope associate will pickup your donation on one of the below mentioned schedule." 
        

        data = {
                'name1' :name1,
                'name2' : name2,
                'email': email,
                'subject':subject,
                'message':message,
                'date1':id_date1,
                'date2':id_date2,
                'date3':id_date3,
                'rad1':rad1,
                'rad2':rad2,
                'rad3':rad3,
                'phone':phone_number

               
            }
        message ='''
            \n Hello {},

            {}
           \n{} between {}
            \n{} between {}
            \n{} between {}

            You will be contacted before the scheduled pickup date on +1{}
            \n Thank You.
            \n -Team GivingHope
        '''.format(data['name1'],data['message'],data['date1'],data['rad1'],data['date2'],data['rad2'],data['date3'],data['rad3'],data['phone'])

        send_mail(data['subject'],message,'',[data['email']],fail_silently=True)
        #send_mail('pick','picksch','givinghopeproj@gmail.com',['@gmail.com'],fail_silently=True)
        return render(request, 'pickup/thanks.html', {'title': 'ThankYou'},)



def datepickerview(request):
        # Get the context from the request.
        context = RequestContext(request)
        # A HTTP POST?
        if request.method == 'POST':
            form = EForm(request.POST)
            # Have we been provided with a valid form?
            if form.is_valid():
                form.save(commit=True)
                return HttpResponse("Successfully added the date to database")
            else:
                # The supplied form contained errors - just print them to the terminal.
                print(form.errors)
        else:
            # If the request was not a POST, display the form to enter details.
            form = EForm()
        
        #send_mail('pick','picksch','givinghopeproj@gmail.com',['.com'],fail_silently=True)
        return render('thanks.html', {'form': form}, context)



