import sys
import requests
from bs4 import BeautifulSoup

url = "http://news.cnyes.com/news/id/3763088"
res = requests.get(url)
soup = BeautifulSoup(res.text,"lxml")

# title
text = soup.find("span",{"itemprop":"headline"}).text
print("title : {0}".format(text))

# source & from
text = soup.find_all("span",{"itemprop":"name"})
print("source : {0}".format(text))

# article
text = soup.find("div",{"itemprop":"articleBody"})# article
print(text)
