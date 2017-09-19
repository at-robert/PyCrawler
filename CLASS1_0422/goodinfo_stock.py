# First thing first, importing all the required libraries
import requests
import re
import pandas as pd
from datetime import datetime
import numpy as np

# Defining the stock we want to get by its ID
# stock_id = 2489

# 中華電
# stock_id = 2412 

# 台灣大哥大
stock_id = 3045


# Defining the url that we're about to call
url = 'http://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID={stock_id}'.format(stock_id=stock_id)

header = {
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3)"\
    " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}
response = requests.get(url=url, headers=header)
response.raise_for_status()

print("Return status = {0}".format(response.status_code))

# Parse the whole HTML web page into several data frames
tables = pd.read_html(response.text)
# Iterate through all the tables and print out the number of column of every table
for idx, el in enumerate(tables):
    if tables[idx].shape[1] == 26:
        print('{0} < Here is the table we want.'.format(tables[idx].shape[1]))
    else:
        # print(tables[idx].shape[1])
        print('Columns = {0} , row = {1}'.format(tables[idx].shape[1],tables[idx].shape[0]))

# We only take the table that satisfies our rule: the number of column must be 8
df = list(filter(lambda x:x.shape[1] == 26, tables))[0]
print(df)