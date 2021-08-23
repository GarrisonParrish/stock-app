import requests

"""TODO: Determine whether a given stock is overvalued or undervalued, based on a range of data."""

"""Description: this script provides a simple way to quickly view a range of stock metrics and estimate a stock's value."""

# P/E Ratio can be found in Fundamental Data (function=OVERVIEW) under the 'PERatio' key
# tons of other metrics are given by this function

apikey: str = 'I6LPH1OE9ZCAIAEM'
symbol: str = 'IBM'
url: str = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ symbol }&apikey={ apikey }'

r = requests.get(url)
data = r.json()

p_e_ratio: str = f"P/E Ratio: { data['PERatio'] }"
print(p_e_ratio)

p_e_ratio: str = f"P/E Ratio: { data['PERatio'] }"

p_e_ratio: str = f"P/E Ratio: { data['PERatio'] }"

p_e_ratio: str = f"P/E Ratio: { data['PERatio'] }"

p_e_ratio: str = f"P/E Ratio: { data['PERatio'] }"
