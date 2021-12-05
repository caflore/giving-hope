from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse

import stripe

stripe.api_key = "sk_test_51K0n2eIoAlYYvDJHoT3lu5opqWkVkQUSuSnuqnBti8O4KsPu2uWn0GfenR1QiUKCz6AG3QTy0QioMAIF8b6oI3Ee0095LShTvk"

# Create your views here.



def index(request):
	organization = {
	'name' : 'American Red Cross',
	'title' : 'American Red Cross Hurricane Ida 2021',
	'subtitle' : 'Delivering hope from the Gulf Coast to the Northeast.',
	'posted_on' : 'October 7, 2021',
	'content' : 'One month after Hurricane Ida struck the United States, the American Red Cross continues to work alongside our partners to deliver vital aid to people still struggling with the heartbreaking damage left behind. From the Gulf Coast to the Northeast, dedicated Red Cross volunteers are there to provide support and comfort. As of September 29, 2021, some 370 people remained in Red Cross and community shelters and emergency lodgings in Louisiana and New Jersey. Since Ida first threatened the U.S., the Red Cross and its partners have provided nearly 40,000 overnight stays. With the help of partners, the Red Cross has provided some 763,000 meals and snacks and distributed nearly 300,000 relief items like comfort kits and cleanup supplies. Trained Red Cross volunteers have made 23,700 contacts providing emotional support, health services and spiritual care for people coping with Ida\'s devastating impact. More than 550 trained Red Cross workers are still supporting relief efforts in person or virtually. In total, some 3,000 total disaster workers have supported Red Cross Ida relief efforts since landfall on August 29, 2021. '
	}

	return render(request, 'donate.html', organization)   
