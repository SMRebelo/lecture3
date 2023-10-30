from django.shortcuts import render
from django import forms # Django has a simpler way to creat forms and we must import it here
from django.http import HttpResponseRedirect # this two fectures are need to use to reverse method so we can add a task and be automaticly redirected to the taskList
from django.urls import reverse 
# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task") # Django shortcut to build forms 
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10) # Adding the fiels to our form such as priority and also add conditions such as min as max values. this will automaticly add the fiels to our form without touching the html file 

def index(request):
    if "tasks" not in request.session: # Here we start with linking the tasks to the useres. i belive only using cach. we must create a table using the console
        request.session["tasks"] = [] # basicly if the user doesnt have a list of task, this will generate a new one
    return render(request, "tasks/index.html",{ # creating a html template to display tasks
        "tasks": request.session["tasks"] # this is adding the varible that contains all my tasks display abouve and saving it in a variable to display at the html 
    })    
    
# Now we´re going to build a function to alow us to add new tasks by using a form
def add(request): 
    if request.method == "POST":
        form = NewTaskForm(request.POST) # This will create an instance of the class NewTaskForm with all data sent in POST method
        if form.is_valid(): # here we are checking if the form its valid and in the line below we have access to that data
            task = form.cleaned_data["task"] # We save the information of the "task" the user submited as we have a variable in the class called task and save it a variable called task.  
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index")) # this django method is used to redirect us to the task list right after we added a new task. this must also be imported abouve
        else: # if the task its not valid then we get the form again but with the existing data so we can change it. we do not get a empty form 
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", { # dont forget to add this view to the urls.py inside this directory
        "form": NewTaskForm() # This is the way to implement the django form shortcut
        
        }) 