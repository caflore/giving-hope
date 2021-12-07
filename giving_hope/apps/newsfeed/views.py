from django.shortcuts import render
from newsapi import NewsApiClient
import requests

newsapi = NewsApiClient(api_key='38e76a44797545e9bd089cccc3520d57')

def newsfeed(request):
    top_headlines = newsapi.get_everything(qintitle='catastrophe OR crisis OR disaster OR starving')
    context = {}
    context['news'] = top_headlines
    return render(request, 'newsfeed/newsfeed.html', context)

def organizations(request):
    url = 'https://api.globalgiving.org/api/public/orgservice/all/organizations/active?api_key=e0cbf2ed-4fbf-43ab-8314-4c1b3d3b2670'
    headers = {'content-type': 'application/json', 'accept': 'application/json'}
    
    context = {}
    context['orgs'] = requests.get(url, headers=headers).json
    return render(request, 'newsfeed/organizations.html', context)
