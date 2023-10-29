from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.utils import timezone
from Homepage.models import Book
from django.contrib.auth.models import User


    
class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content[:20]

    