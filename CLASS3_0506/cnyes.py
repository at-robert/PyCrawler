import requests
from bs4 import BeautifulSoup
import pandas as pd


def getNewsData(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"lxml")
    data = {"title":soup.find("span",{"itemprop":"headline"}).text,
            "info":",".join([_.text for _ in soup.find_all("span",{"itemprop":"name"})]),
            "body":"\n".join([_.text for _ in soup.find("div",{"itemprop":"articleBody"}).find_all('p')]),
            "url":url}
    return data

def listNewsUrls(url):
    res = requests.get(url)
    data = res.json()
    last_page = data['items']['last_page']
    page = 2
    urls = []
    while page <= last_page:
        url = url+"&page={}".format(page)
        res = requests.get(url)
        data = res.json()
        urls.append(["http://news.cnyes.com/news/id/"+str(_['newsId']) for _ in data['items']['data']])
        page += 1
    return sum(urls,[])

urls = listNewsUrls("http://news.cnyes.com/api/v3/news/category/headline?limit=30&startAt=1490889600&endAt=1491839999")
data  = map(getNewsData,urls[0:10])

df = pd.DataFrame(list(data))

print (df)
