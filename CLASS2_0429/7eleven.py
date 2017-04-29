import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

api_url = 'http://emap.pcsc.com.tw/EMapSDK.aspx'
f_data = {
    'commandid':'SearchStore',
    'city':'台北市',
    'town':'信義區'
}
data = requests.post(api_url, data=f_data)
xml = BeautifulSoup(data.content, 'lxml')

tags = ['POIName', 'POIID', 'Address', 'X', 'Y',
        'isDining', 'isATM', 'isIbon', 'isLavatory',
        'isCityCafe']
xml_data = xml.find_all(tags)
stores = list()

while 0 < len(xml_data):
    d = {
        'city': u'台北市',
        'town': u'信義區',
        'storeId': int(''.join(xml_data[0].find_all(text=True))),
        'storeName': ''.join(xml_data[1].find_all(text=True)),
        'long': float(''.join(xml_data[2].find_all(text=True))) / 1000000.0,
        'lat': float(''.join(xml_data[3].find_all(text=True))) / 1000000.0,
        'addr': "".join(xml_data[4].find_all(text=True)),
        'dining': True if ''.join(xml_data[5].find_all(text=True)) == 'Y' else False,
        'lavatory': True if ''.join(xml_data[6].find_all(text=True)) == 'Y' else False,
        'atm': True if ''.join(xml_data[7].find_all(text=True)) == 'Y' else False,
        'cityCafe': True if ''.join(xml_data[8].find_all(text=True)) == 'Y' else False,
        'ibon': True if ''.join(xml_data[9].find_all(text=True)) == 'Y' else False
    }
    stores.append(d)
    del xml_data[:len(tags)]
