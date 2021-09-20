"""Demo of polygon.io REST API interface with daily data."""

from polygon import RESTClient
import datetime
from datetime import timedelta


def main():
    key = "upDqU2P1_iPXrgtFpCRGG5g8fAPAX5mL"

    d = datetime.date.today()
    yesterday = d - timedelta(days=2)

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    with RESTClient(key) as client:
        resp = client.stocks_equities_daily_open_close("AAPL", "2021-06-11")
        print(f"On: {resp.from_} Apple opened at {resp.open} and closed at {resp.close}")
        print(str(d))
        print(yesterday)
    with RESTClient(key) as client2:
        resp2 = client2.stocks_equities_daily_open_close("AAPL", str(d))
        print(f"On: {resp2.from_} Apple opened at {resp2.open} and closed at {resp2.close}")


if __name__ == '__main__':
    main()