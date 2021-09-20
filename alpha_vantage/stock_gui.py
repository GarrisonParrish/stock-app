from tkinter import *
import stock_model

USER: str = "Garrison"
GARRISON_KEY = ''

window = Tk()
window.title("Garristocks")
window.geometry('400x300')

# Prompt user for name
# Click button -> "Welcome, usrname"

# welcome_message = f"Welcome, { usr }"

# ENTER TICKER SYMBOL
# <entry> GO
# TICKER NAME
# OPEN - ###
# HIGH - ###
# LOW - ###
# CLOSE - ###3
# VOLUME - ###
# EXIT BUTTON

# TODO: import model and hook it up to the view
# MVC pattern?
# Only need to call call_ticker() from stock_model.py
# call_ticker(key: str, ticker: str) -> dict
# EX: GOOG = {'1. open': '2738.9800', '2. high': '2766.4300', '3. low': '2728.5750', '4. close': '2760.0400', '5. volume': '618978'}
# Note: this data is for 2021-08-09. It is not current. I'm not sure if the API will directly accept timedelta data.

stock_model.call_ticker(GARRISON_KEY, "GOOG")

# Enter ticker symbol
ticker: str = "..."
ticker_prompt = Label(window, text="Enter a ticker symbol", font=("Helvetica", 20))
ticker_prompt.grid(row=0, column=0)

ticker_entry = Entry(window, width=10)
ticker_entry.grid(row=1, column=0)

# Go button command
def btn_go_clicked():
    ticker = ticker_entry.get()
    if ticker != "":
        ticker_label.configure(text=ticker)

# Go button
btn_go = Button(window, text="Go", font=("Helvetica", 20), command=btn_go_clicked)
btn_go.grid(row=1, column=1)

# Ticker name label
ticker_label = Label(window, text=ticker, font=("Helvetica", 20))
ticker_label.grid(row=2, column=0)

# Stock info grid

# OPEN (4, 0) and (4, 1)
open_lbl = Label(window, text="Open:", font=("Helvetica", 15))
open_lbl.grid(row=4, column=0)

open_data_lbl = Label(window, text="...", font=("Helvetica", 15))
open_data_lbl.grid(row=4, column=1)

# HIGH (5, 0) and (5, 1)
high_lbl = Label(window, text="High:", font=("Helvetica", 15))
high_lbl.grid(row=5, column=0)

high_data_lbl = Label(window, text="...", font=("Helvetica", 15))
high_data_lbl.grid(row=5, column=1)

# LOW (6, 0) and (6, 1)
low_lbl = Label(window, text="Low:", font=("Helvetica", 15))
low_lbl.grid(row=6, column=0)

low_data_lbl = Label(window, text="...", font=("Helvetica", 15))
low_data_lbl.grid(row=6, column=1)

# CLOSE (7, 0) and (7, 1)
close_lbl = Label(window, text="Close:", font=("Helvetica", 15))
close_lbl.grid(row=7, column=0)

close_data_lbl = Label(window, text="...", font=("Helvetica", 15))
close_data_lbl.grid(row=7, column=1)

# VOLUME (8, 0) and (8, 1)
vol_lbl = Label(window, text="Volume:", font=("Helvetica", 15))
vol_lbl.grid(row=8, column=0)

vol_data_lbl = Label(window, text="...", font=("Helvetica", 15))
vol_data_lbl.grid(row=8, column=1)

# Exit button command
def exit_app():
    window.destroy()

# Exit button
btn_exit = Button(window, text="Exit", command=exit_app)
btn_exit.grid(row=9, column=0)

# Enter mainloop
window.mainloop()  # creates an endless application loop that will remain until closed