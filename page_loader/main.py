import os

from page_loader.loader import load_data
from page_loader.storage import generate_file_name, save_content


def download(page_url: str, out_dir: str = os.getcwd()) -> str:
    """
    Download page

    :param page_url: page url
    :param out_dir: output folder
    :return: str
    """
    content = load_data(page_url)
    file_name = generate_file_name(page_url)

    file_path = os.path.join(out_dir, file_name)
    # resourse_path = os.path.splitext(file_path)[0] + "_files"

    save_content(content=content, file_path=file_path)

    return file_path
