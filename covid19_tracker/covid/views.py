from  django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
import requests

def home(request):
    ''' 
     Collecting data from url provided by official website and its secret keys and converting it json data which can be used to 
     fetch the details and display accordingly 
    '''
    url = "https://covid-193.p.rapidapi.com/statistics"
    
    # querystring is fetching country wise data and storing in dict
    querystring = {"country":"India"}
    
    # header stores api keys and host path 
    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "be7f37114bmsh38c0486c35a5050p1bc1e5jsnf574155ad041"
        }
    # response stores the json data from the querystring
    response = requests.request("GET", url, headers=headers, params=querystring).json()

    # dataset stores the response data into dataframe/list and data_init initialize the index value of the dataframe
    dataset = response['response']
    data_init = dataset[0]
    
    # context stores the data in the json formate which can be rendered by django templates
    context = {
        # context gets a dict of 'all','recovered','new','critical cases'
        'all': data_init['cases']['total'],
        'recovered': data_init['cases']['recovered'],
        'deaths': data_init['deaths']['total'],
        'new': data_init['cases']['new'],
        'critical': data_init['cases']['critical'],
    }
    
    
    return render(request, 'index.html', context)
