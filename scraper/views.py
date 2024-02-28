# views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .libgenscraper import LibgenScraper
from .models import Keyword, Book, SearchResult
from .tasks import create_save_dir, download_and_save_file


@api_view(['POST'])
def search_books(request):
    query = request.data.get('query')
    if not query:
        return Response({"error": "Query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    # Perform the search using your scraper
    libgen_scraper = LibgenScraper()
    book_links = libgen_scraper.search_books(query)

    # Save search keyword
    keyword, created = Keyword.objects.get_or_create(keyword=query)
    save_dir = create_save_dir(keyword)
    # Save search results
    for book_link in book_links:
        # Extract book details
        book_details = libgen_scraper.get_book_details(book_link)
        book = Book.objects.create(**book_details)
        SearchResult.objects.create(keyword=keyword, book=book)
        download_and_save_file.delay(book.id, book.file_download_url, save_dir)
        download_and_save_file.delay(book.id, book.image_download_url, save_dir)
        # download_and_save_file.apply_async(args=[book.id, book.file_download_url, save_dir])
        # download_and_save_file.apply_async(args=[book.id, book.image_download_url, save_dir])

    return Response({"message": "Search results saved successfully"}, status=status.HTTP_200_OK)
