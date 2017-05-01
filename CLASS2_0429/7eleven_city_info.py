import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://emap.pcsc.com.tw/lib/areacode.js'
city_data = requests.get(url)

# Defining our regex pattern
regex = r'AreaNode\(\'(.*)\'\, new bu\([0-9]+\,[0-9]+\)\, \'([0-9]{2})\'\)'
matches = re.finditer(regex, city_data.text)
cities = list()

for matchNum, match in enumerate(matches):
    cities.append({
        'city': match.group(1),
        'id': match.group(2)
    })

print(cities)
