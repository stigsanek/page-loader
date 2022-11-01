from page_loader.html_doc import HtmlDoc
from tests import FIXTURES, URLS, BEFORE_FILES, read_file


def test_html_doc():
    """
    Test for HtmlDoc class

    :return:
    """
    expected = read_file(FIXTURES / "updated-page.html")
    content = read_file(BEFORE_FILES["page"])

    html_doc = HtmlDoc(content=content, url=URLS["page"])

    for resourse in html_doc.resourses_urls:
        html_doc.replace_resourse_url(old_url=resourse, new_url="test")

    assert html_doc.content == expected
