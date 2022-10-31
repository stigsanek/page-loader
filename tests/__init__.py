from pathlib import Path

FIXTURES = Path(__file__).parent / "fixtures"


def read_file(file_path) -> str:
    """
    Read file

    :param file_path: file path
    :return: str
    """
    with open(file=file_path, encoding="utf-8") as f:
        return f.read()
