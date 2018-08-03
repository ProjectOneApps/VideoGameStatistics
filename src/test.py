import requests
import json
import numpy
import pandas as pd
import sklearn
import matplotlib
import seaborn
import scipy
from pandas.io.json import json_normalize
import news_api
import twitter_api as ta
import datetime

news = news_api.ApiClient('9c964579f7ea4465855d943ba98552f8')


re = news.get_news_past_six_months('minecraft')

data = json.loads(re)
json_text = json.dumps(data)
df = json_normalize(json_text)

# print(df)

d = datetime.date.today() - datetime.timedelta(days=30)
print(d)
