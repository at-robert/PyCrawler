import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

def download_file(url, form_data):
    local_filename = 'downloaded.csv'
    # NOTE the stream=True parameter
    r = requests.post(url, form_data, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return local_filename

BASE_URL = 'http://mops.twse.com.tw'
api_path = '/mops/web/ajax_t51sb01'
limitIDs = ['sii','otc','rotc','pub']
marketID = 'sii'
postData = {
    "encodeURIComponent": 1,
    "step":               1,
    "firstin":            1,
    "TYPEK":              marketID,
    "code":               ""
}

res = requests.post(
    '{base}{path}'.format(base=BASE_URL, path=api_path),
    data = postData
)

soup = BeautifulSoup(res.text, 'html.parser')
# soup = BeautifulSoup(res.text, 'lxml')
file_name = soup.find('input', {'name': 'filename'}).get('value')
print(file_name)
