import requests
import urllib3

from page_loader.errors import PageLoaderException
from page_loader.logger import log


def load_data(url: str) -> requests.Response:
    """
    Load data from url

    :param url: page url
    :return: requests.Response
    """
    urllib3.disable_warnings()

    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()

        log.debug(f"Request to {url} completed successfully")
        return response

    except requests.RequestException as err:
        log.error(err)
        raise PageLoaderException(err)
