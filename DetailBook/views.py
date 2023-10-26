from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Book, Category
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.mixins import LoginRequiredMixin, SingleObjectMixin

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

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    context = {'book': book}
    return render(request, 'DetailBook/book_detail.html', context)

#class BaseDetailView(SingleObjectMixin, View):
    """A base view for displaying a single object."""

    #def get(self, request, *args, **kwargs):
        #self.object = self.get_object()
        #context = self.get_context_data(object=self.object)
      #  return self.render_to_response(context)
    
#class DetailView(SingleObjectTemplateResponseMixin, BaseDetailView):
    """
    Render a "detail" view of an object.

    By default this is a model instance looked up from `self.queryset`, but the
    view will support display of *any* object by overriding `self.get_object()`.
    """
#@login_required
#class BookDetailView(DetailView):
 #   model = Book
   # context_object_name = "book"
  #  template_name = "book_detail.html"
    #login_url = "/accounts/login/"