from django.urls import path
from .views import home, create_review

app_name = 'ReviewApp'

urlpatterns = [
    path('', home, name='home'),
    path('create-review/', create_review, name='create_review'),
]