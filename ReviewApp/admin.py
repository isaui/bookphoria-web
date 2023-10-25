from django.contrib import admin
from ReviewApp.models import Book, Review
# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "product", "rate", "created_at"]
    readonly_fields = ["created_at"]