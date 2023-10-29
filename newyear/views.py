from django.shortcuts import render
import datetime # we must import the datetime module

# Create your views here.

def index(request):
    now = datetime.datetime.now() # this is how you save the date and time inside a variable 
    return render(request, "newyear/index.html", {# the {} is used to add more context to de function
        "newyear": now.month == 1 and now.day == 1
    })