from django.shortcuts import render
import random

def index(request):
    if 'totalgold' not in request.session:
        request.session['totalgold'] = 0

    return render(request, 'index.html')

def farm(request):
    money = random.randint(10,20)
    request.session['totalgold'] += money 
    context = {
        'mymoney' : request.session['totalgold']
    }
    return render(request, 'index.html',context)


def cave(request):
    money = random.randint(5,10)
    request.session['totalgold'] += money 
    context = {
        'mymoney' : request.session['totalgold']
    }
    return render(request, 'index.html',context)


def house(request):
    money = random.randint(2,5)
    request.session['totalgold'] += money 
    context = {
        'mymoney' : request.session['totalgold']
    }
    return render(request, 'index.html',context)


def casino(request):
    money = random.randint(-50,50)
    request.session['totalgold'] += money 
    context = {
        'mymoney' : request.session['totalgold']
    }
    return render(request, 'index.html',context)
