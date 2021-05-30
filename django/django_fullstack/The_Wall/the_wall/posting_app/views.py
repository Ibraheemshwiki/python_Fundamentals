from django.http.response import HttpResponse
from login_app.models import check_email,Users
from django.shortcuts import render, redirect
from .models import *



def create_message(request):
    user = check_email(request.session['user']['email'])
    messages.objects.create(message = request.POST['textmessage'], user= user)
 
    return redirect('/wall')


def index(request):
    allmessages = messages.objects.all().order_by('-id')
    commentz = comments.objects.all()
 
    context = {
            'name' : request.session['user']['first_name'],
            'lname' : request.session['user']['last_name'],
            'all_messages' : allmessages,
            'comments' : commentz

        }
    return render(request,'wall.html',context)


def create_comment(request):
    user = check_email(request.session['user']['email'])
    
    comments.objects.create(comment = request.POST['textcomment'], user = user, messages = messages.objects.get(id = request.POST['messageid']))
    return redirect('/wall')
    