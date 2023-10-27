from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from .models import Review
from .forms import ReviewForm
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test


# Create your views here.



def is_user_not_admin(user):
    return not user.is_superuser

@csrf_exempt
@user_passes_test(is_user_not_admin)
def review_rate(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        book = Book.objects.get(id=book_id)
        review = request.POST.get("review", "")
        rate = request.POST.get("rate")
        photo = request.FILES.get("photo", None)
        user = request.user
        publish = Review(book=book, review=review, rate=rate, user=user)
        # Check if photo is provided
        if photo:
            publish.photo = photo
        publish.save()
        response_data = {'status': 'success', 'message': 'Review added successfully'}
        return JsonResponse(response_data)
        # return redirect("book_detail", id=book_id) # "book_detail" sesuaiin sm path Detail Book Jocelyn
        # return render (request, "review.html")
