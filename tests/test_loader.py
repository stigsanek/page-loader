from pathlib import Path

import pytest

from page_loader.main import download
from page_loader.storage import generate_file_name

FIXTURES = Path(__file__).parent / "fixtures"


def get_file_data(file_path) -> str:
    """
    Get file data

    :param file_path: file_path
    :return: str
    """
    with open(file=file_path, encoding="utf-8") as f:
        return f.read().strip()


@pytest.mark.parametrize(
    argnames="url, file",
    argvalues=[("https://ru.hexlet.io/courses", "ru-hexlet-io-courses.html")]
)
def test_download(url, file, tmp_path, requests_mock):
    """
    Test for download function

    :param url: page url
    :param file: file name
    :param tmp_path: temp dir
    :param requests_mock: requests_mock object
    :return:
    """
    got = get_file_data(FIXTURES / file)
    requests_mock.get(url, text=got)

    test_dir = tmp_path / "test"
    test_dir.mkdir()

    result_file = download(page_url=url, out_dir=str(test_dir))
    expected = get_file_data(result_file)

    assert got == expected
