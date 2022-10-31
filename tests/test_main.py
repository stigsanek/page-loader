import pytest

from page_loader.main import download
from tests import FIXTURES, read_file


@pytest.mark.parametrize(
    argnames="url",
    argvalues=["https://ru.hexlet.io/courses"]
)
def test_download(url, tmp_path, requests_mock):
    """
    Test for download function

    :param url: page url
    :param tmp_path: temp dir
    :param requests_mock: requests_mock object
    :return:
    """
    expected = read_file(FIXTURES / "ru-hexlet-io-courses.html")
    requests_mock.get(url, text=expected)

    test_dir = tmp_path / "test"
    test_dir.mkdir()

    result_file = download(page_url=url, out_dir=str(test_dir))
    got = read_file(result_file)

    assert got == expected
