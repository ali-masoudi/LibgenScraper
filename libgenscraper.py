from math import ceil
from typing import List
from urllib.parse import quote, urljoin

import requests
from bs4 import BeautifulSoup


class LibgenScraper:
    def __init__(self, base_url='http://libgen.is/'):
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
    def get_book_details(self,bookurl:str):
        pass


# Example usage:
if __name__ == "__main__":
    libgen_scraper = LibgenScraper()
    book_links = libgen_scraper.search_books("python")
    print("Found book links:")
    print(book_links)
    print(len(book_links))
