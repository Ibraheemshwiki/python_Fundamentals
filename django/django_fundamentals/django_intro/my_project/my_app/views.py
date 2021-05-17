from django.shortcuts import render, HttpResponse
def root(request):
    return HttpResponse("I am ROOT!")
    