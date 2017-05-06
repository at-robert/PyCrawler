import requests
import re
import json
import pandas as pd

res = requests.get('https://www.giantcyclingworld.com/store.php')

# first focus on the DataSource fragment
data = re.findall('DataSource.+', res.text)[0]

# explicitily get the data
data = json.loads(re.findall('\[.+\]', data)[0])
# data = json.loads(re.findall('\[.+\]', data)[0])

df = pd.DataFrame(data)

names = ['title', 'address', 'longitude','latitude','enableTime']
names.extend(list(set(df.columns.tolist()) - set(names)))
names

df = df[names]

print (df)
