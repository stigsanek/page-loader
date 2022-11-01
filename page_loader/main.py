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

    file_name = generate_file_name(url)
    file_path = os.path.join(out_dir, file_name)
    response = load_data(url)
    save_content(content=response.text, file_path=file_path)
    log.info(f"write html file: {file_path}")

    with open(file=file_path, encoding="utf-8") as f:
        content = f.read()

    html_doc = HtmlDoc(content=content, url=url)
    res_dir = os.path.splitext(file_name)[0] + "_files"
    download_resourses(out_dir=out_dir, res_dir=res_dir, html_doc=html_doc)
    save_content(content=html_doc.content, file_path=file_path)
    log.debug("page is fully loaded")

    return file_path


def download_resourses(out_dir: str, res_dir: str, html_doc: HtmlDoc):
    """
    Download page resourses

    :param out_dir: output folder
    :param res_dir: resourses dir name
    :param html_doc: HtmlDoc
    :return:
    """
    resourses_urls = html_doc.resourses_urls

    if resourses_urls:
        res_path = os.path.join(out_dir, res_dir)
        os.makedirs(res_path)
        log.debug(f"resourses path: {res_path}")

        bar = ChargingBar('Downloading:', max=len(resourses_urls))

        for res_url in resourses_urls:
            response = load_data(res_url)
            name = generate_file_name(res_url)
            path = os.path.join(res_path, name)

            save_content(content=response.content, file_path=path)
            html_doc.replace_resourse_url(
                old_url=res_url,
                new_url=f"{res_dir}/{name}"
            )
            bar.next()

        bar.finish()
        log.debug("resources are loaded")
