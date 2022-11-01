import pytest
from requests_mock import Mocker

from page_loader.errors import PageLoaderException
from page_loader.loader import load_data
from tests import URLS, BEFORE_FILES, read_file


@pytest.mark.parametrize(argnames="key", argvalues=URLS.keys())
def test_load_data(key: str, requests_mock: Mocker):
    """
    Test for load_data function

    :param key: dictionary key URLS
    :param requests_mock: requests_mock.Mocker
    :return:
    """
    expected = read_file(BEFORE_FILES[key], mode="rb")
    url = URLS[key]
    requests_mock.get(url, content=expected)
    got = load_data(url).content

    assert got == expected


@pytest.mark.parametrize(argnames="url", argvalues=URLS.values())
def test_load_data_exception(url: str, requests_mock: Mocker):
    """
    Test for load_data function

    :param url: dictionary value URLS
    :param requests_mock: requests_mock.Mocker
    :return:
    """
    requests_mock.get(url, status_code=400)

    with pytest.raises(PageLoaderException):
        load_data(url)
