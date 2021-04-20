from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView
import requests
# Create your views here.

from .models import Subscriber

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
    if sub.zipcode != "":
      url = f"https://community-zippopotamus.p.rapidapi.com/us/{sub.zipcode}"
      response = requests.request("GET", url, headers=headers)
      results = response.json()
      place = results['places'][0]['place name']
      sub.placename = place
      if place == 'Seattle':
        city_count['seattle'] += 1
      elif place == 'Bellevue':
        city_count['bellevue'] += 1
      elif place == 'Tacoma':
        city_count['tacoma'] += 1
      elif place == 'Shoreline':
        city_count['shoreline'] += 1
      else:
        city_count['other'] += 1
  return render(request, 'dashboard.html', {
    'subs' : subs,
    'city_count': city_count,
  })


def confirmation(request):
  return render(request, 'confirmation.html')