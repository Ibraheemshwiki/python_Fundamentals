from django.urls import path, include

urlpatterns = [
    path('', include('first_app.urls')),
    path('blogs/', include('first_app.urls')),
    path('blogs/new/', include('first_app.urls')),
    path('blogs/create', include('first_app.urls')),
    path('blogs/<int:number>', include('first_app.urls')),
    path('blogs/<int:number>/edit', include('first_app.urls')),
    path('blogs/<int:number>/delete', include('first_app.urls')),

]
