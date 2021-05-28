from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register', views.register),
    path('done', views.done),
    path('login',views.login),
    path('login_ok',views.success),
    path('logout',views.logout)

]