import os
import re
from urllib.parse import urlparse

from page_loader.errors import PageLoaderException
from page_loader.logger import log

EXTENSION = (".html", ".png", ".jpg", ".jpeg", ".svg", ".css", ".js")


def generate_file_name(url: str) -> str:
    """
    Generate file name from url

    :param url: page url
    :return: str
    """
    parsed_url = urlparse(url.strip())
    part_url, ext = os.path.splitext(parsed_url.hostname + parsed_url.path)

    if ext not in EXTENSION:
        ext = ".html"

    return re.sub(pattern=r"\W|_", repl="-", string=part_url) + ext


def save_content(content, file_path):
    """
    Save content to file

    :param content: content
    :param file_path: file path
    :return:
    """
    folder, _ = os.path.split(str(file_path))

    try:
        if not os.path.exists(folder):
            os.makedirs(folder)

        if isinstance(content, bytes):
            mode = "wb"
            encoding = None
        else:
            mode = "w"
            encoding = "utf-8"

        with open(file=file_path, mode=mode, encoding=encoding) as f:
            f.write(content)

    except OSError as err:
        log.error(err)
        raise PageLoaderException(err)
