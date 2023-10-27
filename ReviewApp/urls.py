from django.urls import path
from .views import create_review

app_name = 'ReviewApp'

urlpatterns = [
    path('review/', create_review, name='review'),
]