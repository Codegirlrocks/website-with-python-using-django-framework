from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from home.models import contact
from django.contrib.messages import constants as messages


# Create your views here.
def index(request):
    context ={
        "variable" : "this is sent"
    } 
    return render(request, 'index.html', context)
   # return HttpResponse(" This is home page")
def about(request):
    return render(request, 'about.html')

    #return HttpResponse(" This is about page")
def service(request):
    return render(request, 'service.html')

    #return HttpResponse(" This is service page")
def contact(request):
    if request.method== "Post":
      email = request.Post.get('email')
      Password = request.Post.get('password')
      contact=contact(email= email, )
      contact.save()
      messages.success(request, 'Profile details updated.')


    return render(request, 'contact.html')

    #return HttpResponse(" This is contact page")
def blog(request):
    return render(request, 'index.html')

    #return HttpResponse(" This is blog page")