from django.urls import path
from .views import events, eventLandingPage


urlpatterns = [
    path('event/', eventLandingPage, name='eventlandingPage'),
]