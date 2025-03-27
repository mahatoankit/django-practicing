from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def testingApp(request):
    return HttpResponse("<h1>This is the testing app</h1>")