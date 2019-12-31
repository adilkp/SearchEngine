import requests
from . import models
from requests.compat import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup

BASE_GOOGLE_URL = 'https://www.google.com/search?query={}'


def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    print(quote_plus(search))
    final_url = BASE_GOOGLE_URL.format(quote_plus(search))
    print(final_url)
    response = requests.get('https://www.google.com/search?query=Artificial%20Intelligence')
    data = response.text
    #print(data)
    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)

