import requests
from bs4 import BeautifulSoup

from author import Author
from isbn import ISBN
from language import Language
from book import Book


def create_authors(value: str):
    authors = []
    for author in value.split(","):
        authors.append(Author(author))
    return authors
def create_languages(value: str):
    languages = []
    for language in value.split(","):
        languages.append(Language(language))
    return languages
def create_cities(value: str):
    cities = []
    for city in value.split(","):
        cities.append(city)
    return cities

def create_isbns(value: str):
    isbns = []
    for isbn in value.split(","):
        isbns.append(isbn)
    return isbns

b = Book()
BASE_URL = 'http://libgen.is/'
response = requests.get(BASE_URL + "book/index.php?md5=AEE7239FFCF7871E1D6687CED1215E22")
assert response.status_code == 200
document = BeautifulSoup(response.content, "html.parser")
for detail in document.findAll('font', {"color": "gray"}):
    field = detail.text.strip().replace(':', '')
    value = detail.next_element.next_element.text.strip()
    print(f"{field}:{value}")
    match field:
        case 'Title':
            b.title = value
        case 'Volume':
            b.volume = value
        case 'Author(s)':
            b.authors = create_authors(value)
        case 'Series' :
            b.series = value
        case 'Periodical':
            b.periodical = value
        case 'Publisher':
            b.publisher = value
        case 'City':
            b.city = create_cities(value)
        case 'Year':
            b.year = value
        case 'Edition':
            b.edition = value
        case 'Language':
            b.language = create_languages(value)
        case 'Pages (biblio\\tech)':
            b.pages = value
        case 'ISBN':
            b.isbn = create_isbns(value)
        case 'ID':
            b.id = value
        case 'Time added':
            b.time_added = value
        case 'Time modified':
            b.time_m = value
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
        case 'ISSN':
            b.issn = value
        case 'UDC':
            b.udc = value
        case 'LBC':
            b.lcb = value
        case 'LCC':
            b.lcc = value
        case 'DDC':
            b.ddc = value
        case 'DOI':
            b.doi = value
        case 'OpenLibrary':
            b.openlibrary = value
        case 'ID':
            b.id = value
        case 'Google':
            b.google = value
        case 'Books':
            b.books = value
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
b.image_url=document.find('img')['src']
b.file_url=document.find('img')['src']

print(b)