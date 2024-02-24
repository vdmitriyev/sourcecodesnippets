#!/usr/bin/env python3
'''
    Downloads file using an URL.
    Dependencies:
        pip install requests
'''

import os
import requests
import urllib.parse as urlparse

def download(url, force_download=False):
    """ Downloads given URL and saves a local file"""

    DATA_DIR = 'data'
    if not os.path.exists(DATA_DIR):
        print('[i] create following folder: {0}'.format(DATA_DIR))
        os.makedirs(DATA_DIR)

    r = requests.get(url, stream=True)

    if r.status_code == 200:
        _urlparse = urlparse.urlparse(url)
        f_name = os.path.join(DATA_DIR, os.path.basename(_urlparse.path))
        if (not os.path.exists(f_name) or force_download):
            print('[i] start download for of the url: {}'.format(url))
            print('[i] target file: {}'.format(f_name))
            with open(f_name, 'wb') as fd:
                for chunk in r.iter_content(chunk_size=1024):
                    fd.write(chunk)
            print('[i] finish download')
    else:
        print('[e] Wrong request status code: {0}'.format(r.status_code))

    return f_name

# file from github
readme_md = "https://raw.githubusercontent.com/vdmitriyev/datasets-links-collection/master/README.md"
fname_readme_md = download(readme_md, True)

print ('[i] Downloaded file: {0}'.format(fname_readme_md))
