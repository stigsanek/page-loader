from pathlib import Path

import pytest
from requests_mock import Mocker

from page_loader.main import download
from tests import FIXTURES, read_file


@pytest.mark.parametrize(
    argnames="url",
    argvalues=["https://ru.hexlet.io/courses"]
)
def test_download(url: str, tmp_path: Path, requests_mock: Mocker):
    """
    Test for download function

    :param url: page url
    :param tmp_path: temp dir
    :param requests_mock: requests_mock.Mocker
    :return:
    """
    expected = read_file(FIXTURES / "ru-hexlet-io-courses.html")
    requests_mock.get(url, text=expected)

    test_dir = tmp_path / "test"
    test_dir.mkdir()

    result_file = download(url=url, out_dir=str(test_dir))
    got = read_file(result_file)

    assert got == expected
