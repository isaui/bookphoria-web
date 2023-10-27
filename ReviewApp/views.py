import datetime
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from .models import Review
from .forms import ReviewForm
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test


# Create your views here.

def home(request):
    return render(request, "home.html")

@user_passes_test(lambda u: not u.is_staff, login_url='/your-login-url/')
@csrf_exempt
def create_review(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        book = Book.objects.get(id=book_id)
        review = request.POST.get("review", "")
        rate = request.POST.get("rate")
        photo = request.FILES.get("photo", None)
        user = request.user
        publish = Review(book_id=book_id, book=book, review=review, rate=rate, user=user)
        # Check if photo is provided
        if photo:
            publish.photo = photo
        publish.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

