from django.shortcuts import render
from newsapi import NewsApiClient
from giving_hope.apps.donations.models import Organization

newsapi = NewsApiClient(api_key='38e76a44797545e9bd089cccc3520d57')

def newsfeed(request):
    top_headlines = newsapi.get_everything(qintitle='catastrophe OR crisis OR disaster OR starving')
    context = {}
    context['news'] = top_headlines
    return render(request, 'newsfeed/newsfeed.html', context)

def organizations(request):
    context = {}
    context['orgs'] = Organization.objects.all()

    return render(request, 'newsfeed/organizations.html', context)
