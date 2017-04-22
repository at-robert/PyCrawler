from IPython.display import clear_output
from datetime import datetime
import requests
import re
import json
import pandas as pd
import numpy as np

q = 'sony'
page = 1
#url = 'http://ecshweb.pchome.com.tw/search/v3.3/all/results?q={q}&page={page}'.format(q=q,page=page)
url = 'http://ecshweb.pchome.com.tw/search/v3.3/all/category/DGBJ/results?q={q}&page={page}&sort=rnk/dc'.format(q=q,page=page)

res = requests.get(url)
res.status_code

print (res.status_code)

if(res.status_code == 200):
    # print (res.json())
    prods = res.json()['prods']
    print (prods)
    df = pd.DataFrame(prods)
    # print (df.head(n=3))
    # df.to_csv('pchome.csv')
