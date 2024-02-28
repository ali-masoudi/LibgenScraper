from django.contrib import admin

from .models import Keyword, Book, SearchResult


# Register your models here.

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'creation_date',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'authors', 'volume', 'series', 'publisher', 'city', 'year', 'is_downloaded')
    list_filter = ('is_downloaded', 'creation_date', 'modification_date')
    search_fields = ('title', 'authors', 'publisher', 'year')


@admin.register(SearchResult)
class SearchResultAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'book', 'book_id', 'creation_date',)
    list_filter = ('keyword', 'creation_date',)
    search_fields = ('book__title', 'keyword__keyword')
