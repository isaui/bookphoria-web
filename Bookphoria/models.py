from django.db import models
from django.contrib.auth.models import User
from django import forms
from Homepage.models import Book
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    liked_book = models.ManyToManyField(Book, related_name='likers', blank=True)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields =  ['full_name', 'liked_book']

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    rating = models.IntegerField(default=5,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
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