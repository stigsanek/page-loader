from page_loader.html_doc import HtmlDoc
from tests import FIXTURES, read_file


def test_html_doc():
    """
    Test for html_doc class

    :return:
    """
    expected = read_file(FIXTURES / "new-ru-hexlet-io-courses.html")
    content = read_file(FIXTURES / "ru-hexlet-io-courses.html")

    html_doc = HtmlDoc(content=content, url="https://ru.hexlet.io/courses")

    for resourse in html_doc.resourses_urls:
        html_doc.replace_resourse_url(resourse, "test")

    assert html_doc.content == expected
