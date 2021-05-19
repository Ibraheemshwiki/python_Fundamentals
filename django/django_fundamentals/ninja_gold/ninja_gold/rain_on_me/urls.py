from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('farm_gold', views.farm),
    path('cave_gold', views.cave),
    path('house_gold', views.house),
    path('casino_gold', views.casino),

]
