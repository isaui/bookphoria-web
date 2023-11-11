import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from DetailBook.forms import CommentForm
from DetailBook.models import Comment
from Homepage.models import Book, Category
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import Count
from Bookphoria.models import UserProfile
from django.contrib.auth.models import User
import json

def home(request):
    return render(request, "home.html")

def get_books(request):
    return render(request, 'get_books.html')

def all_books_page(request):
    return render(request, "allbooks-page.html")

@csrf_exempt
def get_categories(request):
    categories = Category.objects.all()
    categories_list = []
    for category in categories:
        categories_list.append(category.name)
    return JsonResponse({'categories':categories_list})


@csrf_exempt
def get_books_json(request):
    books = Book.objects.prefetch_related('authors', 'images', 'categories').all()
    book_list = []
    for book in books:
        book_data  = {
            'title': book.title,
            'subtitle': book.subtitle,
            'description': book.description,
            'authors': [author.name for author in book.authors.all()],
            'publisher': book.publisher,
            'published_date': book.published_date.strftime('%Y-%m-%d') if book.published_date else None,
            'language': book.language,
            'currencyCode': book.currencyCode,
            'is_ebook': book.is_ebook,
            'pdf_available': book.pdf_available,
            'pdf_link': book.pdf_link,
            'thumbnail': book.thumbnail,
            'categories': [category.name for category in book.categories.all()],
            'images': [imageUrl.url for imageUrl in book.images.all()],
            'price': book.price,
            'saleability': book.saleability,
            'buy_link': book.buy_link,
            'epub_available': book.epub_available,
            'epub_link': book.epub_link,
            'maturity_rating': book.maturity_rating,
            'page_count': book.page_count,
        }
        book_list.append(book_data)
    return JsonResponse({'books': book_list})

#HAMPIR FIXED
def book_detail(request, id):
    book = Book.objects.select_related('user__auth_user').prefetch_related('authors', 'images', 'categories', 'likes').annotate(review_count=Count('review')).get(pk=id)
    user = request.user
    profile = UserProfile.objects.get(user=user) if user.is_authenticated else None
    book_data  = {
            'review_count': book.review_count,
            'likes':  [{'username': user.username, 'userId': user.pk} for user in book.likes.all()],
            'fullname':book.user.auth_user.fullname,
            'username':book.user.auth_user.username,
            'id': book.pk,
            'title': book.title,
            'subtitle': book.subtitle,
            'description': book.description,
            'authors': [author.name for author in book.authors.all()],
            'publisher': book.publisher,
            'published_date': book.published_date.strftime('%Y-%m-%d') if book.published_date else None,
            'language': book.language,
            'currencyCode': book.currencyCode,
            'is_ebook': book.is_ebook,
            'pdf_available': book.pdf_available,
            'pdf_link': book.pdf_link,
            'thumbnail': book.thumbnail,
            'categories': [category.name for category in book.categories.all()],
            'images':[imageUrl.url for imageUrl in book.images.all()],
            'price': book.price,
            'saleability': book.saleability,
            'buy_link': book.buy_link,
            'epub_available': book.epub_available,
            'epub_link': book.epub_link,
            'maturity_rating': book.maturity_rating,
            'page_count': book.page_count,
            'user_publish_time': book.user_publish_time,
    }

    context = {
        'book': book ,
        'user': {
            'id': user.id if user else None,
            'username': user.username if user else None,
            'is_authenticated': True if user else False,
            'profile': profile
        },
        'profile':profile
    }
    return render(request, 'review-book-dummy.html', context)

#FIXED
@csrf_exempt
def add_comment_ajax(request):
    data = json.loads(request.body)
    user = User.objects.get(pk=int(data['userId'])) if data['userId'] else None
    print(user) 
    print(data)
    book = Book.objects.prefetch_related('authors', 'images', 'categories').get(pk=data['bookId'])
    print(book)
    if request.method == 'POST':
        try:
            print('sini lah susah bgt')
            new_comment = Comment(user=user,content=data['content'], book=book)
            print('kemari woi')
            new_comment.save()
            print('nah okee')
            
            return JsonResponse({'status':201})
        except Exception as e:
            print(e)
            return JsonResponse({'status':500})
        
    return HttpResponseNotFound()

def user_profile_serializer(user_profile):
    user_profile_json = serializers.serialize('json', [user_profile])
    return user_profile_json
#FIXED
@csrf_exempt
def get_comment_json(request, book_id):
    comments = Comment.objects.select_related('user__auth_user').filter(book__id=book_id)
    commentList = []
    for comment in comments:
        commentData = {
            'user': comment.user.auth_user.to_dict() if comment.user else None,
            'content':comment.content,
            'created_at':comment.created_at
        }
        commentList.append(commentData)
    return JsonResponse({'comments': commentList},safe=False)