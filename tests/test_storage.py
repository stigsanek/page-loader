import pytest

from page_loader.storage import generate_file_name


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
def test_create_name(url, file_name):
    """
    Test for create_name function

    :param url: page url
    :param file_name: expected name
    :return:
    """
    assert generate_file_name(url) == file_name
