from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('books/', views.books_list, name='books_list'),
   path('books/<int:book_id>/', views.book_detail, name='book_detail'),
]


#path('books/<int:book_id>/', views.book_detail, name='book_detail'),


#  path('people/<int:person_id>/', views.person_detail, name='person_detail')