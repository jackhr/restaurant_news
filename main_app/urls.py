from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subscribers/create/', views.SubscriberCreate.as_view(), name='subscribers_create'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('confirmation/', views.confirmation, name='confirmation'),
]
