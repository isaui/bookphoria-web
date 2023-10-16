from django.urls import path
from .views import home, get_books_json
app_name = 'Homepage'

urlpatterns = [
    path('', home, name='home'),
    path('get-books/', get_books_json, name='get-books' )
]
