import requests

url = "http://news.cnyes.com/api/v3/news/category/headline?limit=30&startAt=1490889600&endAt=1491839999"
res = requests.get(url)
data = res.json()
last_page = data['items']['last_page']
page = 1
urls = []
while page <= last_page:
    url = "http://news.cnyes.com/api/v3/news/category/headline?limit=30&startAt=1490889600&endAt=1491839999&page={}".format(page)
    res = requests.get(url)
    data = res.json()
    print(page,len(data['items']['data']))
    urls.append(["http://news.cnyes.com/news/id/"+str(_['newsId']) for _ in data['items']['data']])
    page += 1
urls = sum(urls,[])
