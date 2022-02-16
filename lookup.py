from tkinter import *

import requests  # for url request --> pip install requests
import json  # for handling json data --> pip install json

import os
os.system('cls')

root = Tk()

root.title("Crypto Portfolio App")
# root.iconbitmap('')

Name = Label(root, text="Name", bg="white", font="verdana 8 bold")
Name.grid(row=0, column=0, sticky=N+S+E+W)

Rank = Label(root, text="Rank", bg="silver", font="verdana 8 bold")
Rank.grid(row=0, column=1, sticky=N+S+E+W)

CurrentPrice = Label(root, text="Current Price", bg="white", font="verdana 8 bold")
CurrentPrice.grid(row=0, column=2, sticky=N+S+E+W)

PricePaid = Label(root, text="Price Paid", bg="silver", font="verdana 8 bold")
PricePaid.grid(row=0, column=3, sticky=N+S+E+W)

PLPer = Label(root, text="P/L Per", bg="white", font="verdana 8 bold")
PLPer.grid(row=0, column=4, sticky=N+S+E+W)

OneHourChange = Label(root, text="1-Hour Change", bg="silver", font="verdana 8 bold")
OneHourChange.grid(row=0, column=5, sticky=N+S+E+W)

TfHourChange = Label(root, text="24-Hour Change", bg="white", font="verdana 8 bold")
TfHourChange.grid(row=0, column=6, sticky=N+S+E+W)

SevenDayChange = Label(root, text="7-Day Change", bg="silver", font="verdana 8 bold")
SevenDayChange.grid(row=0, column=7, sticky=N+S+E+W)

CurrentValue = Label(root, text="Current Value", bg="white", font="verdana 8 bold")
CurrentValue.grid(row=0, column=8, sticky=N+S+E+W)

PLTotal = Label(root, text="P/L Total", bg="silver", font="verdana 8 bold")
PLTotal.grid(row=0, column=9, sticky=N+S+E+W)


# url = 'https://api.nomics.com/v1/currencies/ticker?key=a2bd8a14327d4beac4a8fa484ddd000b52b7c8de&' \
#       'ids=BTC,ETH,XRP,NEWO&interval=1d'
#
# api_response: any = []
#
# try:
#     api_request = requests.get(url)
#     api_response = json.loads(api_request.content)
# except Exception as e:
#     print(e)
#
# my_portfolio = [
#     {
#         "symbol": "BTC",
#         "amount_owned": 1000,
#         "price_paid_per": 2.00
#     },
#     {
#         "symbol": "NEWO",
#         "amount_owned": 100000,
#         "price_paid_per": .01
#     }
# ]
#
#
# for x in my_portfolio:
#     market_price = ''
#     total_paid = float(x['amount_owned']) * float(x['price_paid_per'])
#     current_value = ''
#     profit_loss = ''
#
#     # print(x['name'])
#     # print("${0.2f}".format(float(x['price'])))
#     # print(x['rank'])


def lookup():
    pass


root.mainloop()
