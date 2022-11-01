from pathlib import Path

FIXTURES = Path(__file__).parent / "fixtures"

URLS = {
    "page": "https://ru.hexlet.io/courses",
    "img": "https://ru.hexlet.io/assets/professions/nodejs.png",
    "css": "https://ru.hexlet.io/assets/application.css",
    "js": "https://ru.hexlet.io/script.js",
    "html": "https://ru.hexlet.io/courses"
}

BEFORE_FILES = {
    "page": FIXTURES / "src-page.html",
    "img": FIXTURES / "files" / "nodejs.png",
    "css": FIXTURES / "files" / "application.css",
    "js": FIXTURES / "files" / "script.js",
    "html": FIXTURES / "files" / "courses.html"
}

AFTER_FILES = {
    "page": Path("ru-hexlet-io-courses.html"),
    "img": Path("ru-hexlet-io-courses_files/ru-hexlet-io-assets-professions-nodejs.png"),  # noqa E501
    "css": Path("ru-hexlet-io-courses_files/ru-hexlet-io-assets-application.css"),  # noqa E501
    "js": Path("ru-hexlet-io-courses_files/ru-hexlet-io-script.js"),
    "html": Path("ru-hexlet-io-courses_files/ru-hexlet-io-courses.html")
}


def read_file(file_path: str, mode: str = "r") -> str:
    """
    Read file

    :param file_path: file path
    :param mode: (optional) mode ('r' or 'rb')
    :return: str
    """
    encoding = "utf-8" if mode == "r" else None

    with open(file=file_path, mode=mode, encoding=encoding) as f:
        return f.read()
