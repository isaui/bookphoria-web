from django.forms import SlugField
from django.shortcuts import get_object_or_404, render
from .models import Book

# Create your views here.

def detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    
    context = {
        'book': book 
    }
    return render(request, "book_detail.html", context)