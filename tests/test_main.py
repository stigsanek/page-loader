from pathlib import Path

import pytest
from requests_mock import Mocker

from page_loader.main import download
from tests import FIXTURES, URLS, BEFORE_FILES, AFTER_FILES, read_file


@pytest.fixture
def fake_loads(requests_mock: Mocker):
    """
    Fake requests

    :return:
    """
    for k, v in URLS.items():
        content = read_file(BEFORE_FILES[k], mode="rb")
        requests_mock.get(v, content=content)


def test_download(tmp_path: Path, fake_loads):
    """
    Test for download function

    :param tmp_path: temp dir
    :param fake_loads: fake_loads fixture
    :return:
    """
    test_dir = tmp_path / "test"
    test_dir.mkdir()

    result_file = download(url=URLS["page"], out_dir=str(test_dir))
    exp_content = read_file(FIXTURES / AFTER_FILES["page"])
    got_content = read_file(result_file)

    assert got_content == exp_content

    for k, v in AFTER_FILES.items():
        exp_path = test_dir / v
        assert exp_path.exists()
