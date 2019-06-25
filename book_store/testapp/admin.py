from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','book_name','author_name','published_date','number_of_books','rack_number']

admin.site.register(Book,BookAdmin)
