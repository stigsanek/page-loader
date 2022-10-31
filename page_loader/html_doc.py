from urllib.parse import urlparse, urljoin

from bs4 import BeautifulSoup

ATRR_MAP = {
    "img": "src",
    "script": "src",
    "link": "href"
}


class HtmlDoc:
    """
    HTML document
    """

    def __init__(self, content: str, url: str):
        """
        Constructor

        :param content: html content
        :param url: page url
        """
        self._soup = BeautifulSoup(content, 'html.parser')
        self._resourses = self._parse_resourses_urls(url)

    @property
    def content(self) -> str:
        """
        Get HTML content

        :return: str
        """
        return self._soup.prettify()

    @property
    def resourses_urls(self) -> list:
        """
        Get resourses urls

        :return: list
        """
        return [i[0] for i in self._resourses]

    def _parse_resourses_urls(self, base_url: str) -> list:
        """
        Parse resourses urls

        :return:
        """
        src_url = urlparse(base_url.strip())
        resourses = []

        for t in self._soup.findAll(ATRR_MAP.keys()):
            attr = ATRR_MAP[t.name]
            url = t[attr]

            if not url:
                continue

            parsed_url = urlparse(url)
            is_host = parsed_url.hostname == src_url.hostname

            if is_host or not parsed_url.hostname:
                base_url = f"{src_url.scheme}://{src_url.hostname}"
                new_link = urljoin(base_url, parsed_url.path)
                resourses.append((new_link, attr, t))

        return resourses

    def replace_resourse_url(self, old_url: str, new_url: str):
        """
        Replace resourse url

        :param old_url: old resourse url
        :param new_url: new resourse url
        :return:
        """
        resourses = filter(lambda l: l[0] == old_url, self._resourses)

        for resourse in resourses:
            _, attr, tag = resourse
            tag[attr] = new_url
