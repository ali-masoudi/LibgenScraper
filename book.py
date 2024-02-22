from author import Author
from language import Language
from isbn import ISBN
class Book:
    def __init__(self,
                 title=None,
                 authors=None,
                 publisher=None,
                 languages=None,
                 year=None,
                 volume=None,
                 series=None,
                 periodical=None,
                 city=None,
                 edition=None,
                 pages=None,
                 isbn=None,
                 id=None,
                 time_added=None,
                 time_modified=None,
                 library=None,
                 library_issue=None,
                 size=None,
                 extension=None,
                 bibtex=None,
                 topic=None,
                 tags=None,
                 identifiers=None,
                 issn=None,
                 udc=None,
                 lbc=None,
                 lcc=None,
                 ddc=None,
                 doi=None,
                 openlibrary_id=None,
                 google_books=None,
                 asin=None,
                 book_attributes=None,
                 dpi=None,
                 ocr=None,
                 bookmarked=None,
                 scanned=None,
                 orientation=None,
                 paginated=None,
                 color=None,
                 clean=None,
                 img_url=None,
                 file_url=None):
        self.title = title
        self.volume = volume
        self.authors = authors if authors else []
        self.series = series
        self.periodical = periodical
        self.publisher = publisher
        self.city = city
        self.year = year
        self.edition = edition
        self.language = languages if languages else []
        self.pages = pages
        self.isbn = isbn
        self.id = id
        self.time_added = time_added
        self.time_modified = time_modified
        self.library = library
        self.library_issue = library_issue
        self.size = size
        self.extension = extension
        self.bibtex = bibtex
        self.topic = topic
        self.tags = tags
        self.identifiers = identifiers
        self.issn = issn
        self.udc = udc
        self.lbc = lbc
        self.lcc = lcc
        self.ddc = ddc
        self.doi = doi
        self.openlibrary_id = openlibrary_id
        self.google_books = google_books
        self.asin = asin
        self.book_attributes = book_attributes
        self.dpi = dpi
        self.ocr = ocr
        self.bookmarked = bookmarked
        self.scanned = scanned
        self.orientation = orientation
        self.paginated = paginated
        self.color = color
        self.clean = clean
        self.image_url = img_url
        self.file_url = file_url

    def __str__(self):
        return f'{self.title} - {self.authors}'
