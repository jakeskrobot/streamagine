from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    HttpResponse('This is where the games will reside')
