from django.shortcuts import render,redirect
from .models import *
def index(request):
    context = {
        'dojos' : dojo.objects.all(),
        'ninjas' : ninja.objects.all()
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    dojo.objects.create(name = request.POST['name'], city = request.POST['city'], state = request.POST['state'])
    return redirect('/')

def add_ninja(request):
    ninja.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], dojo= dojo.objects.get(name = request.POST['dojo_select']))

    return redirect('/')
