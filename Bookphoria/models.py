from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django import forms
from Homepage.models import Book
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='auth_user')
    username = models.CharField(max_length=255)
    fullname= models.CharField(max_length=255)
    liked_books = models.ManyToManyField(Book, related_name='users_like', blank=True)
    country = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    profile_picture = models.TextField( blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True) 
    password = models.CharField(max_length = 255, blank=False, null =False)

    def to_dict(self):
        user_data = {
            'user_id': self.user.pk,
            'username': self.username,
            'fullname': self.fullname,
            'country': self.country,
            'city': self.city,
            'age': self.age,
            'profile_picture': self.profile_picture,
            'phone_number': self.phone_number,
            # Anda dapat menambahkan atribut lain sesuai kebutuhan
        }
        return user_data

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields =  ['username',  'fullname', 'password','profile_picture', 'age','phone_number',  'country', 'city' ]

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields =  ['username','fullname', 'password','profile_picture', 'age','phone_number',  'country', 'city']

#class Review(models.Model):
  #  user = models.ForeignKey(User, on_delete=models.CASCADE)
 #   thumbnail = models.URLField(blank=True, null=True)
   # title = models.CharField(max_length=255)
   # rating = models.IntegerField(default=5,
     #   validators=[MinValueValidator(0), MaxValueValidator(5)]
  #  )
  #  photo = models.ImageField(upload_to='review_photos/', blank=True, null=True) # add this
  #  content = models.TextField()
    #created_at = models.DateTimeField(auto_now_add=True)
   # date_added = models.DateField(auto_now_add=True)
   # date_added = models.DateField(default=timezone.now)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

#class ReviewForm(forms.Form):
   # rating = forms.IntegerField(label='Rating', min_value=1, max_value=5)
   # text = forms.CharField(label='Review', widget=forms.Textarea)
