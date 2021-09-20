# stock-app

Hello! This is a simple stock app I created to practice using APIs and to familiarize myself with the JSON data format.
Over the summer of 2021 I became interested in stocks and investment, so this was a fun way to learn more about the market
while learning useful coding skills.

The app is powered by the excellent [Alpha Vantage API](https://rapidapi.com/alphavantage/api/alpha-vantage/). There is currently a rate limit of 5 calls per minute and a hard
limit of 500 calls per day. Unfortunately the cheapest plan is $49.99 a month, so I think I'll stick to the free option.

Current goals for this project:

##  Short-term:
- develop the GUI to look nice
- Add functionality for selecting specific days
- incorporate matplotlib or seaborn to display graphical data for specific stocks


## Long-term:
- mobile support
- more ticker data
- fundamentals data (PEG, etc) and larger market data (S&P500, Dow Jones)
- algorithm for comparing stock's performance to market trends (overvalued or undervalued?)
- massive disclaimer that the algorithm is made by an amateur and will not beat the market


A small note: the code originally contained my personal API key before I realized the repo was public. The original repo was changed but just to be sure I deleted it (better safe than sorry). You can get a free API key from the Alpha Vantage website and paste it wherever the app requires it.

### Update: better GUI framework found
While looking around for a good framework I found PyQt5. It looks pretty well-supported and documented and has cross-platform support, so I'll try to use it for this app. Hopefully this will make it easier to add functionality.

### Update 2: I got a crypto account
I got a Kraken account and there is a place to get an API key. Maybe I could use this for that push notification idea I had earlier? Perhaps I could use Kraken's API with this app to get better crypto data than what Alpha Vantage offers.
