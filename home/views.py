from django.shortcuts   import render
from books.models       import book

# Create your views here.
def get_index(request):
    
    if request.user.is_authenticated:
        book_items  = book.objects.filter(owner=request.user)
    else:
        book_items = []
        
    return render(request, "home/index.html", {'books' : book_items} )