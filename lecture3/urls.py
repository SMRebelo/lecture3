"""
URL configuration for lecture3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path # we must add the include as we are using it beneath 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include("hello.urls")), # Here we are creating a new url named hello/ . this path will include the file urls inside the directory hello. inside the urls.py we already created a path with an empty string "". 
    path('newyear/', include("newyear.urls"))# Here we are creating a new root for the new app "newyear" same as above. 
    
]
