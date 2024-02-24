from math import ceil
from typing import List
from urllib.parse import quote, urljoin

import requests
from bs4 import BeautifulSoup

from author import Author
from book import Book
from isbn import ISBN
from language import Language

BASE_URL = 'https://libgen.is/'


class LibgenScraper:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url
        self.books_url = []

    def search_books(self, query: str) -> List[str]:
        url_param_formatted_string = quote(query)
        search_url = urljoin(self.base_url,
                             f'search.php?req={url_param_formatted_string}&open=0&res=100&view=simple&phrase=1&column=def&sortmode=ASC')
        response = requests.get(search_url)
        response.raise_for_status()
        document = BeautifulSoup(response.content, "html.parser")
        number_of_found_items = int(document.find('font', {"color": "grey", "size": "1"}).text.split()[0])
        print(f"Number of found items={number_of_found_items}")
        max_pages = ceil(number_of_found_items / 100)
        print(f"Max pages to crawl={max_pages}")

        for page_num in range(1, max_pages + 1):
            page_url = search_url + f'&page={page_num}'
            print("extracting page number {}".format(page_num))
            self.books_url.extend(self.extract_book_links(page_url))
        return self.books_url

    def extract_book_links(self, url: str) -> List[str]:
        response = requests.get(url)
        response.raise_for_status()
        document = BeautifulSoup(response.content, "html.parser")
        main_table = document.find('table', {"class": ["c"]})
        if main_table:
            # Removing First Row, AKA (ID,Author(s),Title,Publisher,Year,Pages,Language,Size,Extension,Mirrors,Edit)
            main_table.tr.extract()
            return [urljoin(self.base_url, a['href']) for a in
                    main_table.find_all('a', href=lambda href: href and "book/index.php?md5=" in href)]
        return []

    def create_authors(self, value: str):
        authors = []
        for author in value.split(","):
            authors.append(Author(author))
        return authors

    def create_languages(self, value: str):
        languages = []
        for language in value.split(","):
            languages.append(Language(language))
        return languages

    def create_cities(self, value: str):
        cities = []

        for city in value.split(","):
            cities.append(city)
        return cities if True else ''

    def create_isbns(self, value: str):
        isbns = []
        for isbn in value.split(","):
            isbns.append(ISBN(isbn))
        return isbns

    def get_book_download_url(self, book_download_page_url):
        response = requests.get(book_download_page_url)
        document = BeautifulSoup(response.content, "html.parser")
        return document.find('h2').a['href']

    def get_book_details(self, book_detail_url: str):
        b = Book()
        response = requests.get(book_detail_url)
        document = BeautifulSoup(response.content, "html.parser")
        for detail in document.findAll('font', {"color": "gray"}):
            field = detail.text.strip().replace(':', '')
            value = detail.next_element.next_element.text.strip()
            match field:
                case 'Title':
                    b.title = value
                case 'Volume':
                    b.volume = value
                case 'Author(s)':
                    b.authors = self.create_authors(value)
                case 'Series':
                    b.series = value
                case 'Periodical':
                    b.periodical = value
                case 'Publisher':
                    b.publisher = value
                case 'City':
                    b.city = self.create_cities(value) if len(value) > 1 else ''
                case 'Year':
                    b.year = value
                case 'Edition':
                    b.edition = value
                case 'Language':
                    b.language = self.create_languages(value)
                case 'Pages (biblio\\tech)':
                    b.pages = value
                case 'ISBN':
                    b.isbn = self.create_isbns(value)
                case 'ID':
                    b.id = value
                case 'Time added':
                    b.time_added = value
                case 'Time modified':
                    b.time_modified = value
                case 'Library':
                    b.library = value
                case 'Library issue':
                    b.library_issue = value
                case 'Size':
                    b.size = value
                case 'Extension':
                    b.extension = value
                case 'Topic':
                    b.topic = value
                case 'Tags':
                    b.tags = value
                case 'ISSN':
                    b.issn = value
                case 'UDC':
                    b.udc = value
                case 'LBC':
                    b.lbc = value
                case 'LCC':
                    b.lcc = value
                case 'DDC':
                    b.ddc = value
                case 'DOI':
                    b.doi = value
                case 'OpenLibrary ID':
                    b.open_library_id = value
                case 'ID':
                    b.id = value
                case 'Google Books':
                    b.google_books = value
                case 'ASIN':
                    b.asin = value
                case 'DPI':
                    b.dpi = value
                case 'OCR':
                    b.ocr = value
                case 'Bookmarked':
                    b.bookmarked = value
                case 'Scanned':
                    b.scanned = value
                case 'Orientation':
                    b.orientation = value
                case 'Paginated':
                    b.paginated = value
                case 'Color':
                    b.color = value
                case 'Clean':
                    b.clean = value
        b.image_url = urljoin(self.base_url , document.find('img')['src'])
        b.file_url = self.get_book_download_url(document.find('td', {'rowspan': 22, 'width': 240}).a['href'])
        print(b)


# Example usage:
if __name__ == "__main__":
    libgen_scraper = LibgenScraper()
    book_links = libgen_scraper.search_books("python mastery")
    for book_link in book_links:
        libgen_scraper.get_book_details(book_link)
    print("Found book links:")
    print(book_links)
    print(len(book_links))
