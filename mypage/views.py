from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("hello friends")
def index1(request):
    return HttpResponse("Welcome to my page")
