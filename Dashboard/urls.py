from django.urls import path
from .views import get_profile, add_book, get_books_json
app_name = 'Dashboard'

urlpatterns = [
    path('', get_profile, name='get-profile'),
    path('add-book/', add_book, name='add_book'),
    path('get-books/', get_books_json, name='get-books'),
]
