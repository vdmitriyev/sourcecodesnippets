#!/usr/bin/env python3

__version__ = "1.1"
__description__ = "Find broken links in a webpage"

import os
import time
import urllib.parse as urlparse

import click
import markdown
import requests
from bs4 import BeautifulSoup

CHECK_TIMEOUT_SEC = 0.5


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
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.status_code
    except requests.exceptions.RequestException as e:
        return None


def find_broken_links(html_page: str, debug: bool = False):
    """Parses HTML and returns a list of broken HTTP URLs."""

    broken_links = []
    soup = BeautifulSoup(html_page, "html.parser")

    for link in soup.find_all("a"):
        href = link.get("href")
        if href and href.startswith("http"):
            time.sleep(CHECK_TIMEOUT_SEC)
            if debug:
                print(f"[i] Check URL: {href}")
            status_code = check_url_availability(href)
            if not status_code:
                if debug:
                    print(f"[i] Is not available URL: {href}")
                broken_links.append(href)

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
                click.echo(link)
        else:
            click.echo("[i] no broken links found!")
    else:
        print(f"[e] markdown file was not downloaded: {fname}")


if __name__ == "__main__":
    cli()
