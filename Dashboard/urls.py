from django.urls import path
from .views import get_profile, add_book
app_name = 'Dashboard'

urlpatterns = [
    path('', get_profile, name='get-profile'),
    path('add-book/', add_book, name='add-book'),
]
