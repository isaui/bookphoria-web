from django.forms import ModelForm
from Homepage.models import Book

class BookForm(ModelForm):
  class Meta:
    model = Book
    fields = ['thumbnail', 'authors', 'title', 'categories', 'publisher', 'language', 'page_count', 'published_date', 'currencyCode', 'price', 'description', 'is_ebook', 'pdf_available']
