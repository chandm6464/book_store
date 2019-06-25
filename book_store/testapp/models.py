from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length = 200, unique = True)
    author_name = models.CharField(max_length = 200)
    published_date = models.DateTimeField()
    number_of_books = models.IntegerField()
    rack_number = models.IntegerField()

    def __str__(self):
        return self.book_name
