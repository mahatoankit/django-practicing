from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def events(request):
    return HttpResponse("<h1>This is event section</h1>")