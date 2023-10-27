from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from Homepage.models import Book

# @login_required
def get_profile(request):
    return render(request, 'profile.html')

# @csrf_exempt
# def add_book(request):
#     if request.method == 'POST':
#         author = request.POST.get("author")
#         title = request.POST.get("title")
#         category = request.POST.get("category")
#         publisher = request.POST.get("publisher")
#         language = request.POST.get("language")
#         page_count = request.POST.get("page_count")
#         pub_date = request.POST.get("pub-date")
#         price = request.POST.get("price")
#         user = request.user

#         new_book = Book(author=author, title=title, category=category, publisher=publisher, language=language, page_count=page_count, pub_date=pub_date, price=price, user=user)
#         new_book.save()

#         # return HttpResponse(b"CREATED", status=201)

# # return HttpResponseNotFound()