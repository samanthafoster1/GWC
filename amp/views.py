from django.shortcuts import render

def index (request) :
    return render (request, 'amp/home.html')

# Create your views here.
