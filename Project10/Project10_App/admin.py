from django.contrib import admin

from .models import Author
from .models import Book



class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'country')
    search_fields = ('name', 'country')
    list_filter = ('country',)

admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author')
    list_filter = ('author',)
    ordering = ('-publication_date',)

admin.site.register(Book, BookAdmin)
