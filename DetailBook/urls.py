from django.urls import path
from .views import home, get_books, all_books_page, get_categories, book_detail

app_name = 'DetailBook'

urlpatterns = [
    #path("book/<slug:slug>/", BookDetailView.as_view(), name="detail"),
    #path('book-detail/<slug:slug>/', book_detail, name='book_detail'),
    path('book-detail/<slug:slug>/', book_detail, name='book_detail'),
    path('', home, name='home'),
    path('get-books/', get_books, name='get-books'),
    path('all-books/', all_books_page, name='all-books-page'),
    path('get-categories/', get_categories, name='get-categories'),
]
