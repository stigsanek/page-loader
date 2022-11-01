import pytest
from requests_mock import Mocker

from page_loader.loader import load_data
from tests import FIXTURES, read_file


@pytest.mark.parametrize(
    argnames="url",
    argvalues=["https://ru.hexlet.io/courses"]
)
def test_load_data(url: str, requests_mock: Mocker):
    """
    Test for load_data function

    :param url: page url
    :param requests_mock: requests_mock.Mocker
    :return:
    """
    expected = read_file(FIXTURES / "ru-hexlet-io-courses.html")
    requests_mock.get(url, text=expected)
    got = load_data(url).decode("utf-8")

    assert got == expected
