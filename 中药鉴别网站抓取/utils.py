import requests
import pandas as pd


def get_html(url, header=None, encoding=None):
    try:
        if header is None:
            header = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
            }
        r = requests.get(url, headers=header)
        r.raise_for_status()
        if encoding is not None:
            r.encoding = encoding
        else:
            r.encoding = r.apparent_encoding
        return r.text
    except:
        print('get html error : {}'.format(url))
        return ''
