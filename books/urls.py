from django.conf.urls   import url
from books.views        import add_a_book

urlpatterns = [
    url(r'^add$', add_a_book, name='add_a_book'),
]