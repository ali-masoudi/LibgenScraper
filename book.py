import isbn


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
                 topic=None,
                 tags=None,
                 issn=None,
                 udc=None,
                 lbc=None,
                 lcc=None,
                 ddc=None,
                 doi=None,
                 open_library_id=None,
                 google_books=None,
                 asin=None,
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
        self.city = city if city else []
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
        self.topic = topic
        self.tags = tags
        self.issn = issn
        self.udc = udc
        self.lbc = lbc
        self.lcc = lcc
        self.ddc = ddc
        self.doi = doi
        self.open_library_id = open_library_id
        self.google_books = google_books
        self.asin = asin
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
        author_names = ", ".join(str(author) for author in self.authors)
        language_names = ", ".join(str(language) for language in self.language)
        isbns = ", ".join(str(isbn) for isbn in self.isbn)
        return (f'Title: {self.title}\n'
                f'Volume: {self.volume}\n'
                f'Authors: {author_names}\n'
                f'Series: {self.series}\n'
                f'Periodical: {self.periodical}\n'
                f'Publisher: {self.publisher}\n'
                f'City: {self.city}\n'
                f'Year: {self.year}\n'
                f'Edition: {self.edition}\n'
                f'Languages: {language_names}\n'
                f'Pages: {self.pages}\n'
                f'ISBN: {isbns}\n'
                f'ID: {self.id}\n'
                f'Time Added: {self.time_added}\n'
                f'Time Modified: {self.time_modified}\n'
                f'Library: {self.library}\n'
                f'Library Issue: {self.library_issue}\n'
                f'Size: {self.size}\nExtension: {self.extension}\n'
                f'Topic: {self.topic}\n'
                f'Tags: {self.tags}\n'
                f'ISSN: {self.issn}\nUDC: {self.udc}\nLBC: {self.lbc}\n'
                f'LCC: {self.lcc}\nDDC: {self.ddc}\nDOI: {self.doi}\n'
                f'OpenLibrary ID: {self.open_library_id}\n'
                f'Google Books: {self.google_books}\nASIN: {self.asin}\n'
                f'DPI: {self.dpi}\n'
                f'OCR: {self.ocr}\nBookmarked: {self.bookmarked}\n'
                f'Scanned: {self.scanned}\nOrientation: {self.orientation}\n'
                f'Paginated: {self.paginated}\nColor: {self.color}\n'
                f'Clean: {self.clean}\nImage URL: {self.image_url}\nFile URL: {self.file_url}')
