#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("Hello Frank!. I am home")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("Hello ,I am about")
    return render(request, 'about.html')
