
# Polygon.io API

Polygon.io is a "free" API that provides end-of-day data at the free level and real-time data for the low, low price of $199 a month. I do not have $199 a month so this may not be much more useful than Alpha Vantage in the first place.

Polygon's API uses the WebSocket protocol. WebSocket is distinct from HTTPS and allows for two-way connection. Here, just read the [Wikipedia article](https://en.wikipedia.org/wiki/WebSocket) because I don't fully understand how it works.

From the Polygon.io website:
> Polygon.io provides a standardized interface for streaming real-time stock, forex, and crypto data using the WebSocket protocol. Users can specify which WebSocket channels they want to consume by sending instructions in the form of actions. Our WebSockets emit events to notify the user when an event has occurred in a subscribed channel.

I'm a little worried that this will constantly notify me of events and eventually I'll run out of calls for that minute.

> Access to different feeds varies depending on your subscription. These docs are customized to your version of the API and display your key and data, which only you can see. These docs demonstrate using WebSocket to interact with the API using standardized protocols over TCP.

Big brain stuff. It looks like Polygon offers more options but is a bit harder to use. Either way I'll only be getting historical data, which is only good for past analysis anyway.