from django.shortcuts import render
from django.http import JsonResponse
from .models import Book, Review
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return render(request, "home.html")

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
            'images':[imageUrl.url for imageUrl in book.images.all()],
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

def review_rate(request):
    if request.method == "GET":
        book_id = request.GET.get("book_id")
        book = Book.objects.get(id=book_id)
        review = request.GET.get("review")
        rate = request.GET.get("rate")
        user = request.user
        Review(user=user, book=book, review=review, rate=rate).save()
        return redirect("book_detail", id=book_id)
