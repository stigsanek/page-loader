import os
import re
from urllib.parse import urlparse

import requests
import urllib3


def send_request(url: str) -> requests.Response:
    """
    Send request

    :param url: page url
    :return: requests.Response
    """
    urllib3.disable_warnings()

    response = requests.get(url, verify=False)
    code = response.status_code

    if code == requests.codes.ok:
        return response

    raise requests.HTTPError(f"Loading error. Server response code {code}.")


def create_name(url: str, end_prefix: str = "") -> str:
    """
    Create file name or folder name from url

    :param url: page url
    :param end_prefix: (optional) end prefix or extension
    :return: str
    """
    result = urlparse(url)
    part_url, ext = os.path.splitext(result.netloc + result.path)

    ext = end_prefix if end_prefix else ext
    return re.sub(pattern=r"\W|_", repl="-", string=part_url) + ext


def save_data(data, file_path: str):
    """
    Save data to file

    :param data: data
    :param file_path: file path
    :return:
    """
    folder, _ = os.path.split(file_path)

    if not os.path.exists(folder):
        os.makedirs(folder)

    if isinstance(data, bytearray):
        mode = "w+b"
        encoding = None
    else:
        mode = "w"
        encoding = "utf-8"

    with open(file=file_path, mode=mode, encoding=encoding) as f:
        f.write(data)
