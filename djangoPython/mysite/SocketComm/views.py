from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    html = "<html><body>It is now.</body></html>"
    return HttpResponse(html)

def listen():
    pass