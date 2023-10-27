from django.forms import ModelForm
from ReviewApp.models import Review

@admin.register(Review)
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["id", "user", "book", "rate", "date_added", "photo", "date_added"]
