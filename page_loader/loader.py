import os
import re
from urllib.parse import urlparse

import requests


def load_data(url: str) -> str:
    """
    Download data

    :param url: page url
    :return: str
    """
    response = requests.get(url)
    code = response.status_code

    if code == requests.codes.ok:
        return response.text

    raise requests.HTTPError(f"Loading error. Server response code {code}.")


def save_data(data: str, file_path: str):
    """
    Save data to file

    :param data: data
    :param file_path: file path
    :return:
    """
    folder, _ = os.path.split(file_path)

    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(file=file_path, mode="w", encoding="utf-8") as f:
        f.write(data)


def create_file_name(url: str) -> str:
    """
    Create file name from url

    :param url: page url
    :return: str
    """
    result = urlparse(url)
    part_url, _ = os.path.splitext(result.netloc + result.path)
    return re.sub(pattern=r"\W", repl="-", string=part_url) + ".html"
