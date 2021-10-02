from django.shortcuts import render
from django.https import HttpResponse

#create your views here

def root(request):
    return HttpResponse("The server has started")