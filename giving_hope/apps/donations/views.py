from django.shortcuts import render

def dropoff(request):
    return render(request, 'donations/dropoff.html')