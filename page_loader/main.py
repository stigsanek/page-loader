import os

from page_loader.html_doc import HtmlDoc
from page_loader.loader import load_data
from page_loader.storage import generate_file_name, save_content


def download(url: str, out_dir: str = os.getcwd()) -> str:
    """
    Download page

    :param url: page url
    :param out_dir: output folder
    :return: str
    """
    response = load_data(url)
    file_name = generate_file_name(url)
    file_path = os.path.join(out_dir, file_name)
    res_dir = os.path.splitext(file_name)[0] + "_files"

    html_doc = HtmlDoc(content=response.text, url=url)
    download_resourses(out_dir=out_dir, res_dir=res_dir, html_doc=html_doc)

    save_content(content=html_doc.content, file_path=file_path)
    return file_path


def download_resourses(out_dir: str, res_dir, html_doc: HtmlDoc):
    """
    Download page resourses

    :param out_dir: output folder
    :param res_dir: resourses dir name
    :param html_doc: HtmlDoc
    :return:
    """
    for res_url in html_doc.resourses_urls:
        response = load_data(res_url)
        name = generate_file_name(res_url)
        path = os.path.join(out_dir, res_dir, name)

        save_content(content=response.content, file_path=path)
        html_doc.replace_resourse_url(
            old_url=res_url,
            new_url=f"{res_dir}/{name}"
        )
