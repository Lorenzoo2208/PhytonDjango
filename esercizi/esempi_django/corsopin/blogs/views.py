from django.shortcuts import render
from pprint import pprint
from django.http import HttpResponse, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("index")