import os

from page_loader.loader import load_data, create_file_name, save_data


def download(page_url: str, out_dir: str = os.getcwd()) -> str:
    """
    Download page

    :param page_url: page url
    :param out_dir: output folder
    :return: str
    """
    data = load_data(page_url)
    file_name = create_file_name(page_url)
    file_path = os.path.join(out_dir, file_name)
    save_data(data=data, file_path=file_path)

    return file_path
