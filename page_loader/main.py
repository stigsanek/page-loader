import os

from page_loader.loader import send_request, create_name, save_data


def download(page_url: str, out_dir: str = os.getcwd()) -> str:
    """
    Download page

    :param page_url: page url
    :param out_dir: output folder
    :return: str
    """
    response = send_request(page_url)
    file_name = create_name(url=page_url, end_prefix=".html")
    file_path = os.path.join(out_dir, file_name)
    save_data(data=response.text, file_path=file_path)

    return file_path
