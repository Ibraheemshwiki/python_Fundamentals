from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('show', views.home),
    path('show/new',views.add),
    path('add_new',views.add_new),    
    path('show/<the_id>',views.display_sh),
    path('show/<the_id>/edit',views.edit_Show),
    path('<the_id>/edit', views.do_the_edit),
    path('show/<the_id>/destroy',views.delete),
]