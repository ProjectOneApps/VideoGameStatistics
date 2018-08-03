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

    def get_news_past_six_months(self, startdate, enddate, keyword):

        data = requests.get(self.base_url+'everything?'+'q='+keyword+'&from='+startdate+'&to='+enddate+'&sortBy=popularity'+self.api_key_url)
        if(data.ok):
            jsonData = json.loads(data.content.decode('utf-8'))
            return jsonData
        else:
            print("Unsuccesful: " + str(data.status_code))
            return None
