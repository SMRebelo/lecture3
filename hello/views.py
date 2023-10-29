
from django.http import HttpResponse # imports the build in class of HttpResponse , its basic a print i guess

from django.shortcuts import render


# Create your views here.

def index(request): # function takes the argument of request because it will run acondingly to the url the user will click 
    return HttpResponse("Hello, World!")

def sergio(request):
    return render(request, "Hello/sergio.html")# Here we are passing a argument that its not just a message but a template(hello/sergio.html). this template must be written as well. 

def brian(request):
    return HttpResponse("Hello, Brian!")

def salut(request , name):  
    return HttpResponse(f"Hello, {name.capitalize()}!")# in this case the "name" argument will be written by the user in the url. also added a methode "capitalize" to write the first letter of the name in cap!

def greet(request, name):
    return render(request, "hello/greet.html",{ # Here we add some more context we want the variable to have access to. in this case a dictionary 
        "name": name.capitalize()
    })