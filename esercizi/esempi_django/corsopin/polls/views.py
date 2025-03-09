from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question, Choice
from pprint import pprint

def index(request):
    # queryset = Question.objects.all()
    # pprint(queryset)
    # pprint(queryset[0].choices.all())
    return HttpResponse("Hello, world. You're at the polls index.")