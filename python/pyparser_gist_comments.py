__description__ = 'Parser to fetch comments from GitHub Gist (used for cases when there is not way to revert public gits to secret)'

'''
pip install requests
pip install beautifulsoup4
'''

import requests
from bs4 import BeautifulSoup
import argparse

def parse_gist(url):
    ''' Main function '''

    print (f'[i] Getting comments from the gist under ULR: {url}')
    fname = 'gist-comments.md'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    comments = soup.find_all('td', class_ = 'comment-body')
    output = ''
    verbose = False
    for value in comments:
        if verbose:
            print (value)        
            print(value.text)
        lines = value.text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) > 0:
                #if line.startswith('http'):
                if 'http' in line:
                    output += "* " + line + '\n'
                else:
                    output += '\n' "## " + line + '\n'
        output += '\n'        
        
    with open(fname, 'w', encoding='utf-8') as _f:
        _f.write(output)
    print (f'[i] Check file with comments: {fname}')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument("--url", "-u", help="GitHub gist url", required=True)
    args = parser.parse_args()
    parse_gist(args.url)
