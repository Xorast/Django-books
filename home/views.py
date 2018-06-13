from django.shortcuts   import render
from books.models       import book

# Create your views here.
def get_index(request):
    
    book_items  = book.objects.all()
    
    return render(request, "home/index.html", {'books' : book_items} )