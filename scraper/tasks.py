# tasks.py

import cgi
import os
import time

import requests
from celery import shared_task
from django.conf import settings

from .models import Book

MAX_RETRIES = 5
MEDIA_ROOT = settings.MEDIA_ROOT


@shared_task
def download_and_save_file(book_id, file_url, save_dir):
    retries = 0
    success = False
    while retries < MAX_RETRIES and not success:
        try:
            print("Downloading url {}".format(file_url))
            response = requests.get(file_url, stream=True)
            response.raise_for_status()
            # Extract filename from Content-Disposition header
            filename = get_filename_from_content_disposition(response.headers.get('content-disposition'))
            print('Downloading file {}...'.format(filename))
            save_path = os.path.join(save_dir, filename)
            print('Saving file {}...'.format(save_path))
            save_file(response, save_path)
            update_book(book_id, file_url, save_path)
            success = True
        except requests.RequestException:
            retries += 1
            time.sleep(3)


def update_book(book_id, file_url, save_path):
    try:
        book = Book.objects.get(id=book_id)
        if 'cover' in file_url:
            book.image_download_url = save_path
        else:
            book.file_download_url = save_path
            book.is_downloaded = True
        book.save()
    except Book.DoesNotExist:
        pass


def get_filename_from_content_disposition(content_disposition):
    if content_disposition:
        _, params = cgi.parse_header(content_disposition)
        return params.get('filename')
    return None


def save_file(response, save_path):
    with open(save_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)


def create_save_dir(keyword):
    save_dir = os.path.join(MEDIA_ROOT, f"{keyword.keyword}_{keyword.creation_date}")
    os.makedirs(save_dir, exist_ok=True)
    return save_dir
