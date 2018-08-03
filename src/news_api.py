import requests
import json
import datetime
import dateutil.relativedelta

class ApiClient:

    # date = datetime.date + dateutil.relativedelta.relativedelta(months=-6)

    def __init__(self, api_key):
        self.base_url = 'https://newsapi.org/v2/'
        self.api_key = api_key
        self.api_key_url = '&apiKey=' + self.api_key

    def get_news_past_six_months(self, keyword):

        data = requests.get(self.base_url+'everything?'+'q='+keyword+'&from=2018-01-30'+'&sortBy=popularity'+self.api_key_url).json()
        return data
