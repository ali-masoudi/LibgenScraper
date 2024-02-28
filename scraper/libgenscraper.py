from math import ceil
from typing import List
from urllib.parse import quote, urljoin

import requests
from bs4 import BeautifulSoup

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

    # def create_authors(self, value: str):
    #     authors = []
    #     for author in value.split(","):
    #         authors.append(Author(author))
    #     return authors
    #
    # def create_languages(self, value: str):
    #     languages = []
    #     for language in value.split(","):
    #         languages.append(Language(language))
    #     return languages
    #
    # def create_cities(self, value: str):
    #     cities = []
    #
    #     for city in value.split(","):
    #         cities.append(city)
    #     return cities if True else ''
    #
    # def create_isbns(self, value: str):
    #     isbns = []
    #     for isbn in value.split(","):
    #         isbns.append(ISBN(isbn))
    #     return isbns

    def get_book_download_url(self, book_download_page_url):
        response = requests.get(book_download_page_url)
        document = BeautifulSoup(response.content, "html.parser")
        return document.find('h2').a['href']

    def get_book_details(self, book_detail_url: str):
        book = dict()
        response = requests.get(book_detail_url)
        document = BeautifulSoup(response.content, "html.parser")
        for detail in document.findAll('font', {"color": "gray"}):
            field = detail.text.strip().replace(':', '')
            value = detail.next_element.next_element.text.strip()
            match field:
                case 'Title':
                    book['title'] = value
                case 'Volume':
                    book['volume'] = value
                case 'Author(s)':
                    book['authors'] = value
                case 'Series':
                    book['series'] = value
                case 'Periodical':
                    book['periodical'] = value
                case 'Publisher':
                    book['publisher'] = value
                case 'City':
                    book['city'] = value
                case 'Year':
                    book['year'] = value
                case 'Edition':
                    book['edition'] = value
                case 'Language':
                    book['language'] = value
                case 'Pages (biblio\\tech)':
                    book['pages'] = value
                case 'ISBN':
                    book['isbn'] = value
                case 'ID':
                    book['id'] = value
                case 'Time added':
                    book['time_added'] = value
                case 'Time modified':
                    book['time_modified'] = value
                case 'Library':
                    book['library'] = value
                case 'Library issue':
                    book['library_issue'] = value
                case 'Size':
                    book['size'] = value
                case 'Extension':
                    book['extension'] = value
                case 'Topic':
                    book['topic'] = value
                case 'Tags':
                    book['tags'] = value
                case 'ISSN':
                    book['issn'] = value
                case 'UDC':
                    book['udc'] = value
                case 'LBC':
                    book['lbc'] = value
                case 'LCC':
                    book['lcc'] = value
                case 'DDC':
                    book['ddc'] = value
                case 'DOI':
                    book['doi'] = value
                case 'OpenLibrary ID':
                    book['open_library_id'] = value
                case 'ID':
                    book['id'] = value
                case 'Google Books':
                    book['google_books'] = value
                case 'ASIN':
                    book['asin'] = value
                case 'DPI':
                    book['dpi'] = value
                case 'OCR':
                    book['ocr'] = value
                case 'Bookmarked':
                    book['bookmarked'] = value
                case 'Scanned':
                    book['scanned'] = value
                case 'Orientation':
                    book['orientation'] = value
                case 'Paginated':
                    book['paginated'] = value
                case 'Color':
                    book['color'] = value
                case 'Clean':
                    book['clean'] = value
        book['image_download_url'] = urljoin(self.base_url, document.find('img')['src'])
        book['file_download_url'] = self.get_book_download_url(
            document.find('td', {'rowspan': 22, 'width': 240}).a['href'])
        return book

# Example usage:
# if __name__ == "__main__":
#     libgen_scraper = LibgenScraper()
#     book_links = libgen_scraper.search_books("python mastery")
#     for book_link in book_links:
#         libgen_scraper.get_book_details(book_link)
#     print("Found book links:")
#     print(book_links)
#     print(len(book_links))
