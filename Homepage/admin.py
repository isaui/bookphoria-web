from django.contrib import admin

# Register your models here.
from .models import Book, Author, ImageUrl, Category

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(ImageUrl)
admin.site.register(Category)