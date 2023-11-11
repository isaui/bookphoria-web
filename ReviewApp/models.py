from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.contrib.auth.models import User  # sesuaikan dengan variabel
from Homepage.models import Book,ImageUrl


# Create your models here.
#class Author(models.Model):
 #   name = models.CharField(max_length=100)
  #  def __str__(self):
   #     return self.name

#class ImageUrl (models.Model):
  #  url = models.URLField()
   # def __str__(self):
    #    return self.url

#class Category(models.Model):
 #   name = models.CharField(max_length=50)
  #  def __str__(self):
   #     return self.name



from django.db.models import Q
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_user', null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
   # content = models.TextField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
  #  rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    rating = models.IntegerField(default=5,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    photo = models.ManyToManyField(ImageUrl,related_name='review')
    date_added = models.DateTimeField(default=timezone.now)
    def to_dict(self):
        review_dict = {
            'id': self.id,
            'user_id': self.user.id if self.user else None,
            'book_id': self.book.id,
            'content': self.content,
            'rating': self.rating,
            'date_added': self.date_added,
        }
        return review_dict
    def __str__(self):
        return str('ini konten:'+self.content)