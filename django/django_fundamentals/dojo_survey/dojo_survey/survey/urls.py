from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('creat_user/', views.user_info),
    path('result', views.result),
]