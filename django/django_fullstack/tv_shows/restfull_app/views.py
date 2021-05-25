from django.shortcuts import render,redirect
from .models import *

def index(request):
    return redirect("/show")

def home(request):
    context = {
        "all_the_shows" : Shows.objects.all()
    }
    return render(request, 'index.html',context)

def display_sh(request,the_id):
    get_show = Shows.objects.get(id=int(the_id))
    context = {
        "get_show" : get_show
    }
    return render(request,"show_me.html",context)

def edit_Show(request,the_id):
    get_show = Shows.objects.get(id=int(the_id))

    context = {
        "get_show" : get_show
    }
    return render(request,"edit_show.html",context)
def do_the_edit(request,the_id):
    c = Shows.objects.get(id=int(the_id))
    # 
    t_to_Edit = request.POST['title']
    n_to_Edit = request.POST['network']
    r_to_Edit = request.POST['date']
    d_to_Edit = request.POST['desc']
    # 
    c.title=t_to_Edit
    c.network=n_to_Edit
    c.release_date = r_to_Edit
    c.description=d_to_Edit
    c.save()
    return redirect('/show/' + the_id)

def delete(request,the_id):
    c = Shows.objects.get(id=int(the_id))
    # 
    c.delete()
    return redirect('/show')

def add(request):
    return render(request,"add.html")

def add_new(request):
    
    t_to_create = request.POST['title']
    n_to_create = request.POST['network']
    r_to_create = request.POST['date']
    d_to_create = request.POST['desc']

    show=Shows.objects.create(title=t_to_create,network=n_to_create,release_date=r_to_create,description=d_to_create)
    
    # show_me= Shows.objects.last(
    # 
    return redirect('/show/'+str(show.id))




