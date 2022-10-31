import requests
import urllib3


def load_data(url: str) -> bytearray:
    """
    Load data from url

    :param url: page url
    :return: bytearray
    """
    urllib3.disable_warnings()

    response = requests.get(url, verify=False)
    code = response.status_code

    if code == requests.codes.ok:
        return bytearray(response.content)

    raise requests.HTTPError(f"Loading error. Server response code {code}.")
