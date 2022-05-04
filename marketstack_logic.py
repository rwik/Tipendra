

import os
import requests
import json

API_KEY=os.environ.get('')
BASE_URL = 'http://api.marketstack.com/v1/'


def get_stock_price(symbol):
   #param={access_key=API_KEY}
   params = {
   'access_key': ''
   }
   end_point = ''.join([BASE_URL, 'tickers/', symbol,"/intraday/latest"])
   #print(end_point)
   api_result = requests.get(end_point,params)
   json_result = api_result.json()
   #print(json_result)
   return{
            'open':json_result["open"],
            'high':json_result["high"],
            'low':json_result["low"],
   }

