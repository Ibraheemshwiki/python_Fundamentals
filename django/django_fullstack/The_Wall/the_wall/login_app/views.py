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
    elif request.method == 'POST' :
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['passwd']
        email_check = Users.objects.filter(email=email)
        if email_check :
            return redirect('/wall')
        elif password == request.POST['conpass']:
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


def login(request):
    email = request.POST['email']
    password = request.POST['password']
    use=check_email(request.POST['email'])  

    if use:   
        print(use)
        if bcrypt.checkpw(password.encode(),use.password.encode()):

            
            new_user = Users.objects.get(email = email)
            request.session['user'] = new_user
            request.session['id'] = new_user.id

            return redirect('/login_ok')
        else:
            return redirect('/')
            

def success(request):
    if 'user' in request.session:
       
        return redirect("/wall")
    else :
        return redirect('/')

def logout(request):
    if 'user' in request.session :
        request.session.clear()
        return redirect('/')