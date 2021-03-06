"""Demo of polygon.io REST API interface with aggregate data."""

import datetime
import json
from polygon import RESTClient
from polygon import rest


def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')


def main():
    key = "upDqU2P1_iPXrgtFpCRGG5g8fAPAX5mL"
    ticker: str = input("Input a ticker symbol: ")
    start_date: str = input("Input a dash-separated start date: ")
    end_date: str = input("Input a dash-separated end date: ")

    output_path: str = f"/Users/garrisonparrish/Python Applications/stock-app/data/output:{ticker}:{start_date}:{end_date}.txt"

    get_data(key, ticker, start_date, end_date, output_path)


def get_data(key: str, ticker: str, start_date: str, end_date: str, output_path: str, interval: str = "minute"):
    """Given an API key, ticker symbol, start date, end date, output filepath, and optional interval, writes aggregate data to txt file."""
    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    with RESTClient(key) as client:
        resp = client.stocks_equities_aggregates(ticker, 1, interval, start_date, end_date, unadjusted=False)

        print(f"Minute aggregates for {resp.ticker} between {start_date} and {end_date}.")

        f = open(output_path, "a")
        output_2_path: str = f"/Users/garrisonparrish/Python Applications/stock-app/data/output2:{ticker}:{start_date}:{end_date}.json"
        j = open(output_path, "a")

        json.dump(resp.results, j)

        for result in resp:
            dt = ts_to_datetime(result["t"])
            output_line: str = f"{dt}\n\tO: {result['o']}\n\tH: {result['h']}\n\tL: {result['l']}\n\tC: {result['c']} "
            print(output_line)
            f.write(output_line + '\n')
        
        f.close()
        j.close()

    return output_line


if __name__ == '__main__':
    main()