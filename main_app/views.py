from django.shortcuts import render, HttpResponse
from .forms import SubscriberForm
from django.views.generic.edit import CreateView

# Create your views here.
def home(request):
  return HttpResponse("Hello, world. You're at the Restaurant News Subscriber Network.")

class Subscriber(CreateView):
  model = Subscriber
  fields = "__all__"


