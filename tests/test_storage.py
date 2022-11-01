from pathlib import Path

import pytest

from page_loader.storage import generate_file_name, save_content
from tests import URLS, BEFORE_FILES, AFTER_FILES, read_file


@pytest.mark.parametrize(argnames="key", argvalues=URLS.keys())
def test_generate_file_name(key: str):
    """
    Test for generate_file_name function

    :param key: dictionary key URLS
    :return:
    """
    expected = AFTER_FILES[key].parts[-1]
    got = generate_file_name(URLS[key])

    assert got == expected


def test_save_content(tmp_path: Path):
    """
    Test for save_content function

    :param tmp_path: temp dir
    :return:
    """
    exp_text = read_file(BEFORE_FILES["page"])
    exp_byte = read_file(BEFORE_FILES["img"], mode="rb")

    test_dir = tmp_path / "test"
    test_dir.mkdir()

    page_file = test_dir / AFTER_FILES["page"]
    img_file = test_dir / AFTER_FILES["img"]

    save_content(content=exp_text, file_path=page_file)
    save_content(content=exp_byte, file_path=img_file)

    got_text = read_file(page_file)
    got_byte = read_file(img_file, mode="rb")

    assert exp_text == got_text
    assert exp_byte == got_byte
