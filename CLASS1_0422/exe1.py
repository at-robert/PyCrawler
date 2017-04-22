# First thing first, importing all the required libraries
import requests
import re
import pandas as pd
from datetime import datetime
import numpy as np

#url = 'https://tw.mall.yahoo.com/%E6%B6%B2%E6%99%B6%E8%9E%A2%E5%B9%95-%E9%80%B1%E9%82%8A%E8%A8%AD%E5%82%99-%E9%9B%B6%E7%B5%84%E4%BB%B6-152982959-category.html?.r=1432216228'
url = 'https://tw.search.mall.yahoo.com/search/mall/product?p=sony&qt=product&kw=sony&cid=&clv='
# url = 'https://www.ptt.cc/bbs/Beauty/index.html'

# Defining the stock we want to get by its ID
#stock_id = 2303

# Defining the url that we're about to call
#url = 'https://tw.stock.yahoo.com/d/s/major_{stock_id}.html'.format(stock_id=stock_id)

header = {
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3)"\
    " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}
r = requests.get(url=url, headers=header)
#r = requests.get(url=url)
r.raise_for_status()

print (r.status_code)

if(r.status_code == 200):
    print (r.text)
