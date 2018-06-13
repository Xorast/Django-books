from django.db import models

# Create your models here.
class book(models.Model):
    title   = models.CharField(max_length=200, blank=False)
    author  = models.CharField(max_length=200, blank=False)
    ISBN    = models.CharField(max_length=200, blank=False)
    date    = models.DateField(auto_now=False)
    notes   = models.TextField()
    image   = models.ImageField(upload_to="home/static/media/book_cover", height_field=None, width_field=None, max_length=100)
    
    def __str__ (self):
        return self.title