import requests
import pandas as pd
from bs4 import BeautifulSoup

# Initiate an empty list to store our data
data = []

# Here we're initiating a Session object to keep certain parameters across all our requests
with requests.Session() as s:
    s.headers.update({
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4)'\
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87'\
                      ' Safari/537.36'
    })

    # Fire the Get request on our first try,
    # the purpose is simply to get the view
    # state values
    url = 'http://www.taiwanlottery.com.tw/lotto/Lotto649/history.aspx'
    r = s.get(url)

    # Feeding our response into Beautifulesoup so
    # that it's easier for us to extract the data
    soup = BeautifulSoup(r.content, 'html.parser')

    # Here's the juicy part, we're going to grab
    # these values and save them for our later use
    viewstate  = soup.find('input', {'id': '__VIEWSTATE'         })['value']
    generator  = soup.find('input', {'id': '__VIEWSTATEGENERATOR'})['value']
    validation = soup.find('input', {'id': '__EVENTVALIDATION'   })['value']

    # For demonstration purpose, we only crawl
    # the first three months' data of this year
    for month in range(3, 0, -1):
        res = s.post(
            url=url,
            data={
                'Lotto649Control_history$DropDownList1':  2,
                'Lotto649Control_history$chk':            'radYM',
                'Lotto649Control_history$dropYear':       106,
                'Lotto649Control_history$dropMonth':      month,
                'Lotto649Control_history$btnSubmit':      '查詢',
                '__EVENTTARGET':                          '',
                '__EVENTARGUMENT':                        '',
                '__VIEWSTATE':                            viewstate,
                '__VIEWSTATEGENERATOR':                   generator,
                '__EVENTVALIDATION':                      validation,
                '__LASTFOCUS':                            ''
            }
        )
        # Appending the response into our list
        data.append(res)

        # Here we update the existing view state values with the new ones
        soup = BeautifulSoup(r.content, 'html.parser')
        viewstate  = soup.find('input', {'id': '__VIEWSTATE'         })['value']
        generator  = soup.find('input', {'id': '__VIEWSTATEGENERATOR'})['value']
        validation = soup.find('input', {'id': '__EVENTVALIDATION'   })['value']

print (data)

feb = pd.read_html(data[2].text)

table_feb = list(filter(lambda x:x.shape[1] == 9, feb))
table_feb[0]

table_feb[0] = table_feb[0].transpose()

table_feb[0].columns = table_feb[0].iloc[0]
table_feb[0]

table_feb[0].reindex(table_feb[0].index.drop(0))

print (table_feb[0])
