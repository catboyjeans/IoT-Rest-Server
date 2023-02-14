from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

#tutorial page 
def index(request):
    return HttpResponse("Server is up and running! ^_^")
