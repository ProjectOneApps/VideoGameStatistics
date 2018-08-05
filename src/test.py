import requests
import json
import numpy as np
import pandas as pd
import sklearn
import matplotlib
import seaborn
import scipy
from pandas.io.json import json_normalize
import news_api
import datetime
from pytrends.request import TrendReq

news = news_api.ApiClient('9c964579f7ea4465855d943ba98552f8')

listval = []
for i in range(180, 2, -1):
    s = datetime.date.today() - datetime.timedelta(days=i)     # gets the date from 30 days ago
    e = datetime.date.today() - datetime.timedelta(days=(i-1)) # gets date from 29 days ago need to make into a for loop
    sdate = s.strftime('%Y-%m-%d')                             # converts to a string
    edate = e.strftime('%Y-%m-%d')
    val = news.get_news_past_six_months(sdate, edate, 'fortnite')
    if val is not None:
        totalCount = val['totalResults']
        listval.append(totalCount)

print(listval)

# data = json.loads(re)
# json_text = json.dumps(data)
# df = json_normalize(json_text)

# print('Results are {0}'.format(totalCount))

# testing the google trends api
pytrends = TrendReq()
kw_list = ["Fortnite", "Minecraft", "Grand Theft Auto"]
pytrends.build_payload(kw_list, cat=0, timeframe='all', geo='', gprop='')
print(pytrends.get_historical_interest(kw_list, year_start=2017, month_start=9, day_start=1, hour_start=0, year_end=2018, month_end=8, day_end=1, hour_end=0, cat=0, geo='', gprop='', sleep=0))
