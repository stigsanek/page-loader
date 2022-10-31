import os
import re
from urllib.parse import ParseResult

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


def create_name(parse_res: ParseResult, end_prefix: str = "") -> str:
    """
    Create file name or folder name from url

    :param parse_res: ParseResult
    :param end_prefix: (optional) end prefix or extension
    :return: str
    """
    part_url, ext = os.path.splitext(parse_res.netloc + parse_res.path)

    end = end_prefix if end_prefix else ext
    return re.sub(pattern=r"\W|_", repl="-", string=part_url) + end


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
