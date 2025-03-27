from django.urls import path
from .views import eventRegistration


urlpatterns = [
    path('', eventRegistration, name='eventRegistration')
]
