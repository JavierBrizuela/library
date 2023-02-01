from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return HttpResponse('Este es el inicio')

def fin(request):
    return HttpResponse('este es el fin')

def index(request):
    return HttpResponse('este es el index')

