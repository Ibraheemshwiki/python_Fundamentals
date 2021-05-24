from django.shortcuts import render,redirect
from .models import *

def index(request):
    context = {
        'books' : Books.objects.all()
    }
    return render(request, 'index.html', context)

def book_page(request, book_id):
    this_book = Books.objects.get(id = int(book_id))
    asoc_authors = this_book.authors.all()
    not_asoc_authors = Authors.objects.exclude(books=this_book)
    context = {
        'this_book' : this_book,
        'assoc_authors' : asoc_authors,
        'not_assoc_authors' : not_asoc_authors
        
    }
    return render(request, 'book_info.html', context)

def author_page(request,author_id):
    this_author = Authors.objects.get(id=int(author_id))
    assoc_books = this_author.books.all()
    not_assoc_books = Books.objects.exclude(authors=this_author)
    context = {
        'this_author' : this_author,
        'assoc_books' : assoc_books,
        'not_assoc_books' : not_assoc_books
    }
    return render(request, 'author_info.html',context)

def author_to_book(request, book_id):
    if request.POST['select_author']:
        this_book = Books.objects.get(id = int(book_id))
        this_author = Authors.objects.get(id=request.POST['select_author'])
        this_book.authors.add(this_author)
    return redirect('/book_info/'+str(book_id))

def authors(request):
    context = {
        'authors' : Authors.objects.all()
    }
    return render(request, 'author.html', context)
def addauthor(request):
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    notes = request.POST['note']
    Authors.objects.create(first_name = first_name, last_name=last_name,notes = notes)
    return redirect('/authors')

def addbook(request):
    title = request.POST['title']
    desc = request.POST['desc']
    Books.objects.create(title = title,desc = desc)
    return redirect('/')

def book_to_author(request, author_id):
    if request.POST['select_book']:
        this_author = Authors.objects.get(id = int(author_id))
        this_book = Books.objects.get(id=request.POST['select_book'])
        this_author.books.add(this_book)
    return redirect('/author_info/'+str(author_id))
