import os

from progress.bar import ChargingBar

from page_loader.html_doc import HtmlDoc
from page_loader.loader import load_data
from page_loader.logger import log
from page_loader.storage import generate_file_name, save_content


def download(url: str, out_dir: str = os.getcwd()) -> str:
    """
    Download page

    :param url: page url
    :param out_dir: output folder
    :return: str
    """
    log.info(f"requested url: {url}")
    log.info(f"output path: {out_dir}")

    response = load_data(url)
    file_name = generate_file_name(url)
    file_path = os.path.join(out_dir, file_name)
    res_dir = os.path.splitext(file_name)[0] + "_files"

    log.debug(f"page name: {file_name}")
    log.debug(f"resourses dir: {file_name}")

    html_doc = HtmlDoc(content=response.text, url=url)
    download_resourses(out_dir=out_dir, res_dir=res_dir, html_doc=html_doc)
    save_content(content=html_doc.content, file_path=file_path)

    log.debug("page is fully loaded")

    return file_path


def download_resourses(out_dir: str, res_dir, html_doc: HtmlDoc):
    """
    Download page resourses

    :param out_dir: output folder
    :param res_dir: resourses dir name
    :param html_doc: HtmlDoc
    :return:
    """
    resourses_urls = html_doc.resourses_urls

    if resourses_urls:
        bar = ChargingBar('Downloading:', max=len(resourses_urls))

        for res_url in resourses_urls:
            response = load_data(res_url)
            name = generate_file_name(res_url)
            path = os.path.join(out_dir, res_dir, name)

            save_content(content=response.content, file_path=path)
            html_doc.replace_resourse_url(
                old_url=res_url,
                new_url=f"{res_dir}/{name}"
            )
            bar.next()

        bar.finish()
        log.debug("resources are loaded")
