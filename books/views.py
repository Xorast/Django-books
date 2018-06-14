from django.shortcuts import render, redirect
from .forms           import AddBookForm

# Create your views here.

def add_a_book(request):
    
    if request.method == "POST":
        
        add_book_form = AddBookForm(request.POST, request.FILES)
        
        if add_book_form.is_valid():
        
            book        = add_book_form.save(commit=False)
            book.owner  = request.user
            book.save()
            add_book_form.save()
        
            return redirect("/")
        
    else:
        add_book_form = AddBookForm()

    return render(request, "books/add-a-book.html", {'form': add_book_form})