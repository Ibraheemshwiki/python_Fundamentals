import dsptime
from django.urls import path,include

urlpatterns = [
    path('', include('dsptime.urls')),
]
