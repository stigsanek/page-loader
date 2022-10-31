import pytest

from page_loader.storage import generate_file_name, save_content
from tests import FIXTURES, read_file


@pytest.mark.parametrize(
    argnames="url, file_name",
    argvalues=[
        ("https://ru.hexlet.io/courses",
         "ru-hexlet-io-courses.html"),
        ("https://ru.hexlet.io/courses_list.html",
         "ru-hexlet-io-courses-list.html"),
        ("https://ru.hexlet.io/assets/professions/nodejs.png",
         "ru-hexlet-io-assets-professions-nodejs.png")
    ]
)
def test_generate_file_name(url, file_name):
    """
    Test for generate_file_name function

    :param url: page url
    :param file_name: expected name
    :return:
    """
    assert generate_file_name(url) == file_name


def test_save_content(tmp_path):
    """
    Test for save_content function

    :param tmp_path: temp dir
    :return:
    """
    expected = read_file(FIXTURES / "ru-hexlet-io-courses.html")

    test_dir = tmp_path / "test"
    test_dir.mkdir()
    file_first = test_dir / "first.html"
    file_second = test_dir / "second.html"

    bytes_data = bytes(expected, "utf-8")
    save_content(content=bytearray(bytes_data), file_path=file_second)
    save_content(content=expected, file_path=file_first)

    got_first = read_file(file_first)
    got_second = read_file(file_second)

    assert got_first == got_second == expected
