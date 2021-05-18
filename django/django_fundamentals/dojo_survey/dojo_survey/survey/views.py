from django.shortcuts import render, redirect

def index(request):
    return render(request,'index.html')

def user_info(request):
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    location_from_form = request.POST['locations']
    language_from_form = request.POST['language']
    comments_from_form = request.POST['comments']
    context = {
	"name_temp" : name_from_form,
	"email_temp" : email_from_form,
    "location_temp" : location_from_form,
    "language_temp" : language_from_form,
    "comments_temp" : comments_from_form,
    }
    return  redirect('create_user/')

def result(request):

    return render(request, 'result.html')



