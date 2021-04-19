from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('dashboard', views.dashboard, name='dashboard')
]
