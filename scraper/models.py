from django.db import models


class BaseModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    modification_date = models.DateTimeField(auto_now=True, verbose_name='Modification Date')

    class Meta:
        abstract = True
        ordering = ('pk',)

    def __str__(self):
        raise NotImplementedError("You Must Implement This Method")


class Keyword(BaseModel):
    keyword = models.CharField(max_length=255, verbose_name="Keyword")
    modification_date = None

    def __str__(self):
        return self.keyword

    class Meta:
        verbose_name = "Keyword"
        verbose_name_plural = "Keywords"


class Book(BaseModel):
    id = models.IntegerField(primary_key=True, verbose_name="ID")  # Modified id field to be an integer
    title = models.CharField(max_length=255, verbose_name="Title")
    authors = models.CharField(max_length=255, verbose_name="Authors")
    volume = models.CharField(max_length=255, blank=True, null=True, verbose_name="Volume")
    series = models.CharField(max_length=255, blank=True, null=True, verbose_name="Series")
    periodical = models.CharField(max_length=255, blank=True, null=True, verbose_name="Periodical")
    publisher = models.CharField(max_length=255, blank=True, null=True, verbose_name="Publisher")
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name="City")
    year = models.CharField(max_length=255, blank=True, null=True, verbose_name="Year")
    language = models.CharField(max_length=255, blank=True, null=True, verbose_name="Language")
    edition = models.CharField(max_length=255, blank=True, null=True, verbose_name="Edition")
    pages = models.CharField(max_length=255, blank=True, null=True, verbose_name="Pages")
    isbn = models.CharField(max_length=255, blank=True, null=True, verbose_name="ISBN")
    time_added = models.CharField(max_length=255, blank=True, null=True, verbose_name="Time Added")
    time_modified = models.CharField(max_length=255, blank=True, null=True, verbose_name="Time Modified")
    library = models.CharField(max_length=255, blank=True, null=True, verbose_name="Library")
    library_issue = models.CharField(max_length=255, blank=True, null=True, verbose_name="Library Issue")
    size = models.CharField(max_length=255, blank=True, null=True, verbose_name="Size")
    extension = models.CharField(max_length=255, blank=True, null=True, verbose_name="Extension")
    topic = models.CharField(max_length=255, blank=True, null=True, verbose_name="Topic")
    tags = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tags")
    issn = models.CharField(max_length=255, blank=True, null=True, verbose_name="ISSN")
    udc = models.CharField(max_length=255, blank=True, null=True, verbose_name="UDC")
    lbc = models.CharField(max_length=255, blank=True, null=True, verbose_name="LBC")
    lcc = models.CharField(max_length=255, blank=True, null=True, verbose_name="LCC")
    ddc = models.CharField(max_length=255, blank=True, null=True, verbose_name="DDC")
    doi = models.CharField(max_length=255, blank=True, null=True, verbose_name="DOI")
    open_library_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="OpenLibrary ID")
    google_books = models.CharField(max_length=255, blank=True, null=True, verbose_name="Google Books")
    asin = models.CharField(max_length=255, blank=True, null=True, verbose_name="ASIN")
    dpi = models.CharField(max_length=255, blank=True, null=True, verbose_name="DPI")
    ocr = models.CharField(max_length=255, blank=True, null=True, verbose_name="OCR")
    bookmarked = models.CharField(max_length=255, blank=True, null=True, verbose_name="Bookmarked")
    scanned = models.CharField(max_length=255, blank=True, null=True, verbose_name="Scanned")
    orientation = models.CharField(max_length=255, blank=True, null=True, verbose_name="Orientation")
    paginated = models.CharField(max_length=255, blank=True, null=True, verbose_name="Paginated")
    color = models.CharField(max_length=255, blank=True, null=True, verbose_name="Color")
    clean = models.CharField(max_length=255, blank=True, null=True, verbose_name="Clean")
    image_save_url = models.URLField(blank=True, null=True, verbose_name="Image Save URL")
    image_download_url = models.URLField(blank=True, null=True, verbose_name="Image Download URL")
    file_save_url = models.URLField(blank=True, null=True, verbose_name="File Save URL")
    file_download_url = models.URLField(blank=True, null=True, verbose_name="File Download URL")
    is_downloaded = models.BooleanField(default=False, verbose_name="Is Downloaded")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


class SearchResult(BaseModel):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE, related_name='search_results')

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='search_results')
    modification_date = None

    class Meta:
        verbose_name = 'Search Result'
        verbose_name_plural = 'Search Results'

    def __str__(self):
        return f"Keyword: {self.keyword.keyword} - Book: {self.book.title}"
