from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,'index.html')




def register(request):
    errors = Users.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['passwd']
        if password == request.POST['conpass']:
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            Users.objects.create(first_name= first_name, last_name = last_name, email= email,password=pw_hash)
            data = {
                'email' : email,
                'password' : password,
                'first_name' : first_name,
                'last_name' : last_name,
            }
            request.session['user'] = data
            return redirect('/login_ok')

        else:
            return redirect('/')


def done(request):
    messages.success(request, 'Account created successfully!')
    return render(request, 'index.html')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    use=check_email(request.POST['email'])     
    if use:   
        print(use)
        if bcrypt.checkpw(request.POST['password'].encode(),use.password.encode()):

            data = {
                'email' : email,
                'password' : password,
                'first_name' : use.first_name,
                'last_name' : use.last_name,
            }
            request.session['user'] = data
            return redirect('/login_ok')
        else:
            return redirect('/')
            

def success(request):
    if 'user' in request.session:
        context = {
            'name' : request.session['user']['first_name']
        }
        return render(request, 'welcome.html', context)

    return redirect('/')

def logout(request):
    if 'user' in request.session :
        request.session.clear()
        return redirect('/')