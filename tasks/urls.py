from django.urls import path 

from . import views

app_name = "tasks" # We give a name the the url path because of name colision, meaning that if we have two path with the name "index", they will colide. and if we give a name the the app  this wount happend.
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]
