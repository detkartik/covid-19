from  django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
import requests

def home(request):
    data = []
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"India"}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "be7f37114bmsh38c0486c35a5050p1bc1e5jsnf574155ad041"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    
    d = response['response']
    s = d[0]

    context = {
        'all': s['cases']['total'],
        'recovered': s['cases']['recovered'],
        'deaths': s['deaths']['total'],
        'new': s['cases']['new'],
        'critical': s['cases']['critical'],
    }
    
   

    return render(request, 'index.html', context)