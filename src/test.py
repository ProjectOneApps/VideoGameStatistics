import requests
import json
import numpy
import pandas
import sklearn
import matplotlib
import seaborn
import scipy
import news_api

news = news_api.ApiClient('9c964579f7ea4465855d943ba98552f8')

url = ('https://newsapi.org/v2/everything?'
       'q=Fortnite&'
       'from=2018-01-30&'
       'sortBy=popularity&'
       'apiKey=9c964579f7ea4465855d943ba98552f8')

response = requests.get(url).json()
re = news.get_news_past_six_months('fortnite')
print(re)
