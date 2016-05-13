#rom django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#def addperson(request):


@csrf_exempt
def printPersons(request):
     print request.body
     method = request.method
     o=request.body.decode("utf-8")
     
     print(json.loads(o))
     #p=Person(name=.name , birthYear=.birthYear , deathYear=.deathYear)
     #p.save()
     return HttpResponse("added 1 entry in person table")


