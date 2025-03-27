from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def eventRegistration(request):
    return HttpResponse("<h1>This is event registration section</h1>")