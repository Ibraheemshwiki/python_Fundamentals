from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('create_user', views.user_info),
    path('bring_it', views.bring_it)
]