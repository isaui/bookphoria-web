from django.db import models
from django.contrib.auth.models import User
from django import forms
from Homepage.models import Book

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    liked_book = models.ManyToManyField(Book, related_name='likers', blank=True)
    country = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True) 

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields =  ['full_name', 'profile_picture', 'age','phone_number',  'country', 'city', 'liked_book', ]

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

class ReviewForm(forms.Form):
    rating = forms.IntegerField(label='Rating', min_value=1, max_value=5)
    text = forms.CharField(label='Review', widget=forms.Textarea)