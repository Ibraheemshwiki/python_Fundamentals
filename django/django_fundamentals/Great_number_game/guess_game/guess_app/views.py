from django.shortcuts import render
import random

def index(request):
    del request.session['counter']
    result = int(random.randint(1, 100))
    request.session['resultF'] = result
    return render(request, 'index.html')

def calculate(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    temp = request.POST['the_guess']
    request.session['tempF'] = temp

    if request.session['resultF'] > int(request.session['tempF']):
        request.session['ni'] = 'low'
    if request.session['resultF'] < int(request.session['tempF']):
       request.session['ni'] = 'high'
    if request.session['resultF'] == int(request.session['tempF']):
        request.session['ni'] = 'win'
   
    context = {
        'variable' : request.session['ni'],
        'the_num' : request.session['resultF'],
        'counter' : request.session['counter']
   }
    return render(request,'index.html', context)