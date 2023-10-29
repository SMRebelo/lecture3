from django.shortcuts import render

# Create your views here.
tasks = ["foo", "bar", "baz"] # fisrts things first, this varible is to learn how to simply show tasks

def index(request):
    return render(request, "tasks/index.html",{ # creating a html template to display tasks
        "tasks": tasks # this is adding the varible that contains all my tasks display abouve and saving it in a variable to display at the html 
    })    
    
# Now we´re going to build a function to alow us to add new tasks by using a form
def add(request): 
    return render(request, "tasks/add.html") # dont forget to add this view to the urls.py inside this directory