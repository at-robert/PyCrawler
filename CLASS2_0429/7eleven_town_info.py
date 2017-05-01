import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

api_url = 'http://emap.pcsc.com.tw/EMapSDK.aspx'
form_data = {
    'commandid': 'GetTown',
    'cityid': '01' # for the purpose of this demo
                   # we're hard-coding 01 for 台北市 here
}
data = requests.post(api_url, data=form_data)
xml = BeautifulSoup(data.content, 'xml')

towns = list()
for el in xml('TownName'):
    towns.append(el.text)

print(towns)
