from  django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
import requests

def home(request):
    data = []
    url = "https://covid-193.p.rapidapi.com/statistics"
    #     Getting data from api with following url

    querystring = {"country":"India"}
#     Querystring contains the data specific to country (eg: India)

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "be7f37114bmsh38c0486c35a5050p1bc1e5jsnf574155ad041"
        }
#      Storing in headers the api host url and keys 
    response = requests.request("GET", url, headers=headers, params=querystring).json()
#      response is storing the json data recieved from url   
    d = response['response']
#     d converts response data into a list to get data frame
    s = d[0]
#     s initialize the response data

    context = {
        'all': s['cases']['total'],
        'recovered': s['cases']['recovered'],
        'deaths': s['deaths']['total'],
        'new': s['cases']['new'],
        'critical': s['cases']['critical'],
    }
#     context gets a dict of 'all','recovered','new','critical cases'
    
   

    return render(request, 'index.html', context)
'''    django templates render this context data into index.html  
navigate to index.html to check the html display for context data
'''
