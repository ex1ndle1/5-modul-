from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book

def home(request):
    return HttpResponse('hi')

def books_list(request):
    books = Book.objects.all()
    return render(request, 'bookshop/books_list.html', {'book': books})






def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.number_of_views += 1
    book.save(update_fields=['number_of_views'])
    return render(request, 'bookshop/book_detail.html', {'book':book})
   





# def person_list(request):
#     people = Person.objects.all()
#     return render(request, 'main/person_list.html', {'people': people})

# def person_detail(request, person_id):
#     person = get_object_or_404(Person, id=person_id)
#     return render(request, 'main/person_detail.html', {'person': person})


