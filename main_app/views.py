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
  return HttpResponse("Hello, world. You're at the Restaurant News Subscriber Network.")

class SubscriberCreate(CreateView):
  model = Subscriber
  fields = '__all__'

def dashboard(request):

  pass

def confirmation(request):
  pass