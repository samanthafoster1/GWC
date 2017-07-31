from django.shortcuts import render

def index (request) :
    return render (request, 'amp/home.html')

def profile (request):
    return render (request, 'amp/basic.html', {'content':['Message me to connect','samanthafoster223@gmail.com'] })

def messaging (request) :
    return render (request, 'amp/messaging.html', { 'content': ['Text me']})

# Create your views here.
