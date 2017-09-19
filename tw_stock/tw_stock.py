# First thing first, importing all the required libraries
import requests
import re
import pandas as pd
from datetime import datetime
import numpy as np

import matplotlib.pyplot as plt
# %matplotlib inline

# Defining the stock we want to get by its ID
year = 2016
stock_ticker = 'TPE:2412'

# Defining the url that we're about to call
url = 'https://www.google.com/finance/historical?q={stock_ticker}&startdate=Sep%{year}%2C%201970&start=0&num=9999'.format(stock_ticker=stock_ticker,year=year)

header = {
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3)"\
    " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}
response = requests.get(url=url, headers=header)
response.raise_for_status()

print('response code = {0}'.format(response.status_code))


# Parse the whole HTML web page into several data frames
tables = pd.read_html(response.text)

# Iterate through all the tables and print out the number of column of every table
for idx, el in enumerate(tables):
    if tables[idx].shape[1] == 6:
        print('{0} < Here is the table we want.'.format(tables[idx].shape[1]))
    else:
        print('Columns = {0} , row = {1}'.format(tables[idx].shape[1],tables[idx].shape[0]))

# We only take the table that satisfies our rule: the number of column must be 8
df = list(filter(lambda x:x.shape[1] == 6, tables))[0]
df.columns = ['Date','Open','High','Low','Close','Volume']
df.drop(0, inplace=True)

df['Date'] = pd.to_datetime(df['Date'])
df2 = df.set_index('Date')

df2['Open'] = pd.to_numeric(df2['Open'])
df2['High'] = pd.to_numeric(df2['High'])
df2['Low'] = pd.to_numeric(df2['Low'])
df2['Close'] = pd.to_numeric(df2['Close'])
df2['Volume'] = pd.to_numeric(df2['Volume'])

print(df2.head())

df2['Open'].plot(label = 'Ch Tel TW', figsize=(16,8))
# plt.show()