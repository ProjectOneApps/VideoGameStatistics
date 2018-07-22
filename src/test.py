import requests
import numpy
import pandas
import sklearn
import matplotlib
import seaborn
import scipy


url = ('https://newsapi.org/v2/everything?'
       'q=Fortnite&'
       'from=2018-01-30&'
       'sortBy=popularity&'
       'apiKey=9c964579f7ea4465855d943ba98552f8')

response = requests.get(url).json()

print(response)
