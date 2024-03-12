__version__ = "1.2"
__description__ = "Find broken links in a markdown"

import os
import re
import sys
import time
import traceback
import urllib.parse as urlparse

import click
import markdown
import requests
from bs4 import BeautifulSoup

CHECK_TIMEOUT_SEC = 0.2


def download(url: str, force_download: bool = False) -> str:
    """Downloads given URL and saves a local file"""

    DATA_DIR = "data"
    if not os.path.exists(DATA_DIR):
        click.echo("[i] create following folder: {0}".format(DATA_DIR))
        os.makedirs(DATA_DIR)

    r = requests.get(url, stream=True)

    if r.status_code == 200:
        _urlparse = urlparse.urlparse(url)
        f_name = os.path.join(DATA_DIR, os.path.basename(_urlparse.path))
        if not os.path.exists(f_name) or force_download:
            click.echo("[i] start download for of the url: {}".format(url))
            click.echo("[i] target file: {}".format(f_name))
            with open(f_name, "wb") as fd:
                for chunk in r.iter_content(chunk_size=1024):
                    fd.write(chunk)
            click.echo("[i] finish download")
    else:
        click.echo("[e] Wrong request status code: {0}".format(r.status_code))

    return f_name


def markdown_to_html(fname):
    md_content, html = None, None
    with open(fname, "r", encoding="utf-8") as _f:
        md_content = "\n".join(_f.readlines())
    if md_content is not None:
        html = markdown.markdown(md_content)
    with open(fname + ".html", "w", encoding="utf-8") as _f:
        _f.write(html)
    return html


def check_url_availability(url: str):
    """Checks if a URL is accessible and returns its status code."""

    response, result, message = None, None, None
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        result, message = response.status_code, "OK"
    except requests.exceptions.ConnectTimeout as ex:
        click.echo(traceback.format_exc())
        result, message = 408, ex
    except Exception as ex:
        click.echo(traceback.format_exc())
        result, message = -1, ex
        if response is not None:
            result = response.status_code

    return result, message


def _find_urls(text: str):
    """
    This function finds URLs in a given text using regular expressions.

    Args:
        text: The text to search for URLs.

    Returns:
        A list of URLs found in the text.
    """

    url_regex = r"""(?i)\b((?:https?://|ftp://|www\.)\S+[^\s.,;?])"""
    urls = re.findall(url_regex, text)

    return urls


def _find_plain_elements(bs_html, search_text: str = "http"):
    elements_found = []
    _elements = bs_html.find_all()
    for el in _elements:
        if el.string and search_text in el.string:
            elements_found.extend(_find_urls(el.string))

    return elements_found


def _find_href_elements(bs_html):
    elements_found = []
    for link in bs_html.find_all("a"):
        href = link.get("href")
        if href and href.startswith("http"):
            elements_found.append(href)

    return elements_found


def _check_broken_links(urls: list, debug: bool = False) -> list:
    broken_links = []
    for url in urls:
        time.sleep(CHECK_TIMEOUT_SEC)
        if debug:
            print(f"[i] Check URL: {url}")

        status_code, message = check_url_availability(url)
        if status_code >= 200 and status_code <= 399:
            if debug:
                print(f"[i] Is not available URL: {url}")
            broken_links.append({"url": url, "code": status_code, "message": message})

    return broken_links


def _log_traceback(ex, ex_traceback=None):
    """Logs exceptions"""
    if ex_traceback is None:
        ex_traceback = ex.__traceback__
    tb_lines = [line.rstrip("\n") for line in traceback.format_exception(ex.__class__, ex, ex_traceback)]
    print(tb_lines)


def find_broken_links(html_page: str, debug: bool = False):
    """Parses HTML and returns a list of broken HTTP URLs."""

    broken_links = []
    soup = BeautifulSoup(html_page, "html.parser")
    broken_links = []
    with_href_tag = _find_href_elements(soup)
    if debug:
        print(f"[i] with_href_tag\n\ttotal: {len(with_href_tag)}\n\turls: {with_href_tag}\n", flush=True)
    broken_links.extend(_check_broken_links(with_href_tag))
    no_href_tag = _find_plain_elements(soup, search_text="https")
    if debug:
        print(f"[i] no_href_tag\n\ttotal: {len(no_href_tag)}\n\turls: {no_href_tag}\n", flush=True)
    broken_links.extend(_check_broken_links(no_href_tag))

    return broken_links


@click.group()
@click.version_option(version=__version__)
def cli():
    pass


@cli.command()
@click.option(
    "--url",
    prompt=False,
    required=False,
    help="The URL of the webpage to scan",
    default="https://raw.githubusercontent.com/vdmitriyev/datasets-links-collection/master/README.md",
)
def check(url):

    fname = download(url, True)
    click.echo("[i] downloaded file: {0}".format(fname))

    if os.path.exists(fname):

        html_page = markdown_to_html(fname)
        broken_links = find_broken_links(html_page, debug=True)

        if broken_links:
            click.echo("[i] broken links found:")
            for link in broken_links:
                click.echo(click.style("=> ", fg="red") + f'{link["code"]}\t{link["url"]}')
        else:
            click.echo("[i] no broken links found!")
    else:
        print(f"[e] markdown file was not downloaded: {fname}")


@cli.command()
@click.option(
    "--url",
    prompt=False,
    required=True,
    help="The URL of the webpage to use for test ",
    default="https://raw.githubusercontent.com/vdmitriyev/datasets-links-collection/master/README.md",
)
def test(url):
    code, message = check_url_availability(url)
    print(code)
    print(message)


if __name__ == "__main__":
    cli()
