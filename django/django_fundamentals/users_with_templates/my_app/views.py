from django.shortcuts import render, redirect
from .models import users

def index(request):
    context = {
    	"users": users.objects.all()
    }
    return render(request, "index.html", context)
def add(request):
    users.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], email_address = request.POST['email'], age = request.POST['age'])
    return redirect('/')
