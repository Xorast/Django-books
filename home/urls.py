from django.conf.urls   import url
from home.views         import get_index

urlpatterns = [
    url(r'^$', get_index,    name='homepage'),
]
