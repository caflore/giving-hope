
#from typing_extensions import Concatenate
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse, request
from django.views import View
from .models import *
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.core.mail import send_mail
import re

import stripe

# Create your views here.


stripe.api_key = settings.SECRET_KEY


def index(request):
    return render(request, 'payment/index.html')

def donation(request):

	try:
		if request.method == 'POST':
			#print('DONE', request.POST)

			amount = int(request.POST['amount'])
			email=request.POST['email']
			name=request.POST['nickname']
			det = (amount,"&",email,"&",name)
			#amount=  round(amount,2)

			customer = stripe.Customer.create(
				email=request.POST['email'],
				name= request.POST['nickname'],
				source=request.POST['stripeToken']
			)
			
			charge = stripe.Charge.create(
				customer=customer,
				amount =amount*100,
				currency='usd',
				description ='Giving Hope Donation',
			)
			
			return redirect(reverse('success',args=[det]))
			
	except Exception as e:
		print(e)
		return str(e)
	
def successMsg(request, args):
	det = args
	
	a= det.split(",")

	# amt =a.split("(")
	# print('amt ',amt[1])

	# em =c.split("'")
	# print('amt ',em[1])

	# nam =d.split("'")
	# print('amt ',nam[1])

	amt= a[0]
	amt=amt.split("(")
	amt=amt[1]
    
	name = a[4]
	name=name.split("'")
	name=name[1]


	eml = a[2]
	eml=eml.split("'")
	eml=eml[1]
	

	name1 = name
	toemail = eml
	subject = 'Donation Update'
	message = "Giving Hope appreatiates your kind gesture for a Donation of amount $" 
	

	data = {
			'name1' :name1,
			'email': toemail,
			'subject':subject,
			'message':message,
			'amt':amt
		 }
	message ='''
		\n Hello {},

		{}{}.00

		\n Thank You.
        \n -Team GivingHope
    '''.format(data['name1'],data['message'],data['amt'])

	send_mail(data['subject'],message,'',[data['email']],fail_silently=False)
	return render(request, 'payment/success.html', {'det':det})



# class baseview(TemplateView):
# 	template_name ='home.html'


# class CreateCheckoutView(View):
# 	def post(self, request, *args, **kwargs):
# 		YOUR_DOMAIN = "http://127.0.0.1:8000/"
# 		checkout_session = stripe.checkout.Session.create(
# 			payment_method_types = ['card'],
# 			line_items = [
# 				 {
# 					'price_data': {
# 						'currency': 'usd',
# 						'unit_amout': 2000,
# 						'product_data': {
# 							'name':'ABC'
# 							},
# 					},
# 					'quantity': 1,
# 				},
#             ],
#             mode='payment',
#             success_url=YOUR_DOMAIN + '/success.html',
#             cancel_url=YOUR_DOMAIN + '/cancel.html',
#         )
# 		return JsonResponse({
# 			'id' : checkout_session.id
# 		})

# def successMsg(request, args):
# 	amount = args
# 	return render(request, 'payment/success.html', {'amount':'amount'})

# def about(request):
#     return render(request, 'payment/about.html', {'title': 'About'})