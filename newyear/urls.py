from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index") # creating the new path for our new app "newyears"
]
