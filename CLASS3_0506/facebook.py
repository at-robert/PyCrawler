# load library
import requests
import json

token='EAACEdEose0cBADLN4hkXi0UgZCZAMqoFDBOiePj9adjtZBIYaufiVzdyYx0NKlu0pX4yDZAPLqhmnSfJPn54IuRoISSZCnAtMEwfmJeUZCigZBZCpdFpXDFkKl490bjR6NUcEL39DVCizxzyWMjxeTmn29SNJZBTxFn0ZCKKxaZCUKZBuiZAX04xUyB7Mx0MWOZBxQ3VMZD'

# get data via Graph API (use string formatting to deal with long variable)
url = "https://graph.facebook.com/v2.8/me?fields=id,name&access_token={}".format(token)
res = requests.get(url)
print(res)


# get your own posts data
url = "https://graph.facebook.com/v2.8/me?fields=id,name,posts&access_token={}".format(token)
res = requests.get(url)

data = res.json()
print(data)

# use header information to escape robot-check
url = "https://graph.facebook.com/v2.8/me?fields=id,name,posts&access_token={}".format(token)
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"}
res = requests.get(url,headers=header)
print(res)
