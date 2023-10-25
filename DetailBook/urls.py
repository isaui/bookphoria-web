from django.urls import path
from .views import detail


urlpatterns = [
    path('detail/<slug:slug>//', detail, name='detail')
]

