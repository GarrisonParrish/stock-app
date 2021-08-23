from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import numpy as np
# import json


GARRISON_KEY = 'I6LPH1OE9ZCAIAEM'

DEBUG = 1

"""
TODO: 
    Add time functionality (test if time entered is in the future or otherwise invalid)
    Add error messages and catch exceptions
    Integrate visual data with pandas (long-term)
    Calculate metadata (running averages, percent increase over time intervals, etc.)
    Implement notifications to provide alerts when a stock hits a certain point (long-term)
    Allow user to select a specific metric and compare to other metrics
"""

def main():
    ticker_data: dict = select_ticker()
    # EX: GOOG = {'1. open': '2738.9800', '2. high': '2766.4300', '3. low': '2728.5750', '4. close': '2760.0400', '5. volume': '618978'}
    
    # data, meta_data = ts.get_intraday('GOOGL')
    # ts = TimeSeries(key='YOUR_API_KEY',tries=5)

    # plt.scatter(, ticker_data['1. open'])

def select_ticker() -> dict:
    key: str = input('Please enter your API key: ').upper() or GARRISON_KEY  # API key
    ticker: str = input("Please enter a ticker symbol: ").upper()  # user inputs ticker symbol
    ticker_data: dict = call_ticker(key, ticker)

    return ticker_data

def call_ticker(key: str, ticker: str) -> dict:
    ts = TimeSeries(key)

    # this is actually a JSON object. Python converts it to a dict for us automatically
    ticker_data, meta = ts.get_daily(symbol=ticker)

    ticker_data_yesterday = ticker_data['2021-08-09']  # dict

    open: float = ticker_data_yesterday['1. open']
    high: float = ticker_data_yesterday['2. high']
    low: float = ticker_data_yesterday['3. low']
    close: float = ticker_data_yesterday['4. close']
    volume: float = ticker_data_yesterday['5. volume']

    if DEBUG == 1:
        print(f'Stock data for { ticker }')
        print(ticker_data_yesterday)
        print(f'Open: ${ open }')
        print(f'High: ${ high }')
        print(f'Low: ${ low }')
        print(f'Close: ${ close }')
        formatted_volume = "{:,}".format(int(volume))  # formats integer into string with comma-separated thousand places
        print(f'Volume: { formatted_volume }')

    return ticker_data_yesterday


if __name__ == '__main__':
    main()