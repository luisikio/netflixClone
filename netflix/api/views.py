from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse ('hola mundo')
def about(request):
    return HttpResponse ('hola about')    

# Create your views here.
