import requests
from bs4 import BeautifulSoup

url = 'https://tw.news.yahoo.com/%E5%AD%98%E8%82%A1%E5%85%A9%E9%A0%AD%E8%B3%BA-%E5%B0%88%E5%AE%B6%E8%AA%AA%E9%80%99%E9%BA%BC%E5%81%9A%E5%B0%B1%E5%B0%8D%E4%BA%86-040151525--finance.html'

import urllib.parse
print(url)

print(urllib.parse.unquote(url))

res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

text = soup.find(itemprop='headline').get_text()
print (text)
text = soup.find(itemprop='url').get_text()
print (text)

soup.find('time', itemprop='datePublished')['datetime']
