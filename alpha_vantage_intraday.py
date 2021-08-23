import requests
import matplotlib.pyplot as plt
import numpy as np
import json
# import pprint
from datetime import datetime

"""
EXAMPLE:

import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
r = requests.get(url)
data = r.json()

print(data)

"""

"""
TIME_SERIES_INTRADAY -> Popular, returns current data trailing 1-2 months. Best for short-term charting. 
Includes extended trading hours where applicable (4 AM to 8 PM for US market). Raw and adjusted.

TIME_SERIES_INTRADAY_EXTENDED -> Returns historical data for the trailing 2 years. Used for longer-term visualization,
trading simulation, and machine learning algorithms. Raw and adjusted.

TIME_SERIES_DAILY -> Returns raw data (as-traded) for the past 20+ years of historical data

TIME_SERIES_DAILY_ADJUSTED -> Popular, returns raw and adjusted data.

TIME_SERIES_WEEKLY -> Returns endpoints for each week, 20+ years trailing.

...

GLOBAL_QUOTE -> Lighter than TIME_SERIES, returns price and volume.

SYMBOL_SEARCH -> Useful for building search functions, returns simple data for chosen symbol.

Also available: Fundamental Data, Forex, Cryptocurrencies, Economic Indicators, Technical Indicators

"""

# demo of TIME_SERIES_INTRADAY
url = "https://alpha-vantage.p.rapidapi.com/query"  # url of the API


querystring = {"interval":"30min","function":"TIME_SERIES_INTRADAY","symbol":"MSFT","datatype":"json","output_size":"compact"}
# interval (required): the real time between queried data points (military time -> 1min, 5min, 15min, 30min, 60min)
# function (required): the type of data being queried (see TIME_SERIES_DAILY, TIME_SERIES_MONTHLY_ADJUSTED, etc.)
# symbol (required): the ticker symbol being tracked
# apikey (required): key to call API, can specify "demo"
# adjusted (optional): enabled by default, true=output time series adjusted by historical split and dividend events
# datatype (optional): format of output, json by default, can also specify csv
# outputsize (optional): compact by default -> compact = last 100 data points in time series, full = full-length time series


headers = {
    'x-rapidapi-key': "d2836a50a9msh78aa72aa3ce55bfp1ace07jsn7df473c419c6",
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)  ## type: class 'requests.models.Response'

# print(response)

# plt.scatter(, ticker_data['1. open'])

# TODO: make a scatter plot of stock data for the day with a 5-minute interval
# PROBLEMS: 
#   getting time data in a manageable format
#   matplotlib.scatter(x, y) -> each argument must be an array or float
#   must convert response to array. Need JSON data.

# print(response.text)
# print(response.json())

"""
with open('stock-data.txt', 'w') as outfile:  # we will create stock-data.txt in the local directory
    json.dump(response.json(), outfile, indent=4)  # json.dump will write to outfile. Second argument could be a socket, but here it is a txt file.
    # should I write to a txt file or a json file?
    # writing with pretty-printing will make it more readable (simple as adding indent=4)
    # we will need to read this data to use it
"""

with open('stock-data.txt') as json_file:
    data = json.load(json_file)  # Deserializes a file to a Python object (dict in this case)
    
    for p in data['Time Series (30min)']:
        # print(f"Time: { p }")
        # print(p.strftime("%Y"))
        
        date_time_obj = datetime.strptime(p, '%Y-%m-%d %H:%M:%S')
        # print('st' if date_time_obj.day == 1 else 'th')

        # TODO: make this a switch case (thanks Guido)
        day_suffix: str = ''
        if (date_time_obj.day == 1):
            day_suffix = 'st'
        elif (date_time_obj.day == 2):
            day_suffix = 'nd'
        elif  (date_time_obj.day) == 3:
            day_suffix = 'rd'
        else:
            day_suffix = 'th'

        print(date_time_obj.strftime(f'The year is %Y. The month is %B. The day is the %-d{ day_suffix }. Time %H:%M:%S'))
        print(f"Open price: ${ data['Time Series (30min)'][p]['1. open'] }")

# request with 30min interval, then once it's working change to 5
# print(response.text)
# TODO: Get this data into an array and throw it into matplotlib or seaborn. Remember: for a stock app, speed is paramount.