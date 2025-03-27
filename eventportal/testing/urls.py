from django.urls import path
from .views import testingApp



urlpatterns =[
    path('', testingApp, name='testingApp')
]