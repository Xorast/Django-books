from django         import forms
from .models        import book
from django.contrib.auth.models import User


class AddBookForm(forms.ModelForm):
    """
    Used by the user to enter a new book to their list
    """
    class Meta:
        model       = book
        fields      = ['title', 'author', 'ISBN', 'date', 'notes', 'image']