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
  return HttpResponse("Hello, world. You're at the Restaurant News Subscriber Network.")

class SubscriberCreate(CreateView):
  model = Subscriber
  fields = '__all__'

def dashboard(request):
  subs = Subscriber.objects.all()
  for sub in subs:
    url = f"https://community-zippopotamus.p.rapidapi.com/us/{sub.zipcode}"
    response = requests.request("GET", url, headers=headers)
    results = response.json()
    place = results['places'][0]['place name']
    sub.placename = place
  return render(request, 'dashboard.html', {
    'subs' : subs,
    'citylookup' : CITYLOOKUP
  })


def confirmation(request):
  return render(request, 'confirmation.html')