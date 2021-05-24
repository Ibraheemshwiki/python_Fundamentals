from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('addauthor',views.addauthor),
    path('addbook', views.addbook),
    path('author', views.authors),
    path('book_info/<int:book_id>', views.book_page),
    path('authortobook/<int:book_id>', views.author_to_book),
    path('author_info/<int:author_id>', views.author_page ),
    path('booktoauthor/<int:author_id>', views.book_to_author),

]