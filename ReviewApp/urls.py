from django.urls import path
from .views import review_rate

app_name = 'ReviewApp'

urlpatterns = [
    path('review/', review_rate, name='review'),
]