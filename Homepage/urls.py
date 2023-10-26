from django.urls import path
from .views import home, get_books_json, all_books_page, get_categories
app_name = 'Homepage'

urlpatterns = [
    path('', home, name='home'),
    path('get-books/', get_books_json, name='get-books' ),
    path('all-books/', all_books_page, name='all-books-page'),
    path('books-get-categories/', get_categories, name='get-categories'),
]
