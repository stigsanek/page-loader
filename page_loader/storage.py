import os
import re
from urllib.parse import urlparse

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

    :param content: data
    :param file_path: file path
    :return:
    """
    folder, _ = os.path.split(str(file_path))

    if not os.path.exists(folder):
        os.makedirs(folder)

    if isinstance(content, bytearray):
        mode = "w+b"
        encoding = None
    else:
        mode = "w"
        encoding = "utf-8"

    with open(file=file_path, mode=mode, encoding=encoding) as f:
        f.write(content)
