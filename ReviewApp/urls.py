from django.urls import path
from .views import home, create_review, get_review_json, show_review

app_name = 'ReviewApp'

urlpatterns = [
    path('get-review/<int:id>', get_review_json, name='get_review_json'),
    path('create-review/', create_review, name='create_review'),
    path('show-review/', show_review, name='show_review'),
]