from django.shortcuts import render, redirect
import requests
from api_key import key

# Create your views here.
def index(request):
    api_key = key['key']
    url = "https://api.thecatapi.com/v1/images/search"
    querystring = {"format":"json"}
    headers = {
    'Content-Type': "application/json",
    'x-api-key': api_key
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    cats = response.json()
    print("Cats: {}".format(cats))
    context = {
        'cats': cats,
    }
    return render(request, 'cat_api/index.html', context)