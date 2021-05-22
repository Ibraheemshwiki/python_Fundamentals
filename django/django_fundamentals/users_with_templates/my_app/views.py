from django.shortcuts import render, redirect, HttpResponse
from .models import users

def index(request):
    context = {
    	"users": users.objects.all()
    }
    return render(request, "index.html", context)
def add(request):
    users.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], email_address = request.POST['email'], age = request.POST['age'])
    return redirect('/')

def get(request, number):
    
    context = {
       'name' : users.objects.get(id=number)
    }
    
    return render(request, 'index2.html', context)

