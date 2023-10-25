from django.urls import path
from .views import home, get_books_json, review_rate

app_name = 'ReviewApp'

urlpatterns = [
    path('', home, name='home'),
    path('get-books/', get_books_json, name='get-books'),
    path('review/', review_rate, name='review'),
]