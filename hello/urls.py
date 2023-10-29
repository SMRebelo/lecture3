# we have to create this file for the directory hello so we can nav that directory 

#too create a url we must first import 
from django.urls import path 

from . import views # we must import the views file. the  from "." means we are importing from this directory 

urlpatterns = [ #this creates a urls paths so we can nav the directory 
    path("", views.index, name="index"),# we are creating a path here to run the function index in the views file. imagine this as tree for all the funtions we create # here empty string "" means no addicional argument 
    path("brian" , views.brian, name="brian"),
    path("sergio", views.sergio, name="sergio"), # in this new function im adding "sergio" to the url, so when i type it the function will apear
    path("<str:name>", views.greet, name="greet")# here we indicate the url to be a srting, that will recive a name that we will give whem we are typing the url ourselfs
]
