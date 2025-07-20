from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    output = "\n".join([f"{book.title} by {book.author}" for book in books])
    return HttpResponse(output, content_type="text/plain")
