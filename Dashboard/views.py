from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from Homepage.models import Book

# @login_required
def get_profile(request):
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
            'user_publish_time': book.user_publish_time
        }
        book_list.append(book.thumbnail)
        # print(book.thumbnail)
        # print(book_list)
        context = {'books':book_list}
    return render(request, 'profile.html', context)

@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        user = request.user
        author = request.POST.get("author")
        title = request.POST.get("title")
        category = request.POST.get("category")
        publisher = request.POST.get("publisher")
        language = request.POST.get("language")
        page_count = request.POST.get("page_count")
        pub_date = request.POST.get("pub-date")
        currencyCode = request.POST.get("currencyCode")
        price = request.POST.get("price")

        new_book = Book(author=author, title=title, category=category, publisher=publisher, language=language, page_count=page_count, pub_date=pub_date, currencyCode=currencyCode, price=price, user=user)
        new_book.save()

        print(Book.objects.get(user=user))  

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()