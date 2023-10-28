from django.urls import path
from .views import get_profile
app_name = 'Dashboard'

urlpatterns = [
    path('', get_profile, name='get-profile'),
]
