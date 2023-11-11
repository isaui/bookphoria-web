import datetime
import json
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, HttpResponseNotFound

from Homepage.models import Book
from .models import Review
from .forms import ReviewForm
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.core import serializers
from django.contrib.auth.decorators import login_required
from Homepage.models import Book,ImageUrl
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request, "home.html")

@csrf_exempt
def get_review_json(request,id):
    book = Book.objects.get(id=id)
    reviews = Review.objects.prefetch_related('photo').select_related('user__auth_user').filter(book=book)
    review_list = []
    
    for review in reviews:
        print(photo.url for photo in review.photo.all())
        review_data  = {
            'user': review.user.auth_user.to_dict() if review.user else None,
            'rating': review.rating,
            'content': review.content,
            'created_at':review.date_added,
            'review':review.to_dict(),
            'photos': [photo.url for photo in review.photo.all()]
        }
        review_list.append(review_data)

    return JsonResponse({'reviews': review_list})

@login_required(login_url='/login/')
def show_review(request):
    form = ReviewForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        create_review(request)
        return HttpResponseRedirect(reverse('ReviewApp:show_review'))
    bookId = 1
    print("==============KINGDOM BOOK==============")
    print(bookId)
    reviews = Review.objects.all()
    context = {
        'name' : request.user.username,
        'reviews' : reviews,
        'form': form,
    }
    return render(request, 'review.html', context)

# def create_review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST or None)
#         if form.is_valid() and request.method == "POST":
#             review = form.save(commit=False)
#             review.user = request.user
#             review.save()
#             return HttpResponseRedirect(reverse('ReviewApp:show_review'))
#     else:
#         form = ReviewForm()
#         context = {'form': form }
#     return render(request, "book_detail.html", context)

@csrf_exempt
def create_review(request):
    data = json.loads(request.body)
    user = User.objects.get(pk=int(data['userId'])) if data['userId'] else None
    print(user) 
    print(data)
    print('konten->',data['content'])
    book = Book.objects.prefetch_related('authors', 'images', 'categories').get(pk=int(data['bookId']))
    print(book)
    if request.method == 'POST':
        try:
            print('sini lah susah bgt')
            new_comment = Review(user=user,rating=int(data['rating']),book=book,content=data['content'])
            print('kemari woi')
            new_comment.save()
            print(new_comment)
            print('nah okee')
            urls = []
            for url in data['photo']:
                photourl, created = ImageUrl.objects.get_or_create(url=url)
                urls.append(photourl)
            new_comment.photo.add(*urls)
            return JsonResponse({'status':201})
        except Exception as e:
            print(e)
            return JsonResponse({'status':500})
        
    return HttpResponseNotFound()