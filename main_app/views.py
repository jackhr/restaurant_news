from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView
import requests
# Create your views here.

from .models import Subscriber

CITYLOOKUP = (
  'Bellevue',
  'Tacoma', 
  'Seattle',
  'Shoreline'
)

headers = {
  'x-rapidapi-key': "b1556901c0mshdb68c001ae12d6ap1d57e6jsnad1a723950e1",
  'x-rapidapi-host': "community-zippopotamus.p.rapidapi.com"
}

def home(request):
  return render(request, 'home.html')

class SubscriberCreate(CreateView):
  model = Subscriber
  fields = ['first_name', 'last_name', 'email', 'zipcode', 'special_date', 'special_date_name', 'phone', 'frequency']

def dashboard(request):
  subs = Subscriber.objects.all()
  city_count = {
    'seattle': 0,
    'bellevue': 0,
    'tacoma': 0,
    'shoreline': 0,
    'other': 0,
  }
  for sub in subs:
    url = f"https://community-zippopotamus.p.rapidapi.com/us/{sub.zipcode}"
    response = requests.request("GET", url, headers=headers)
    results = response.json()
    place = results['places'][0]['place name']
    sub.placename = place
    if sub.placename == 'Seattle':
      city_count['seattle'] += 1
    elif sub.placename == 'Bellevue':
      city_count['bellevue'] += 1
    elif sub.placename == 'Tacoma':
      city_count['tacoma'] += 1
    elif sub.placename == 'Shoreline':
      city_count['shoreline'] += 1
    else:
      city_count['other'] += 1

  return render(request, 'dashboard.html', {
    'subs' : subs,
    'citylookup' : CITYLOOKUP,
    'city_count': city_count,
  })


def confirmation(request):
  return render(request, 'confirmation.html')