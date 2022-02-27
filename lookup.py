from tkinter import *

import matplotlib.pyplot as plt

import requests  # for url request --> pip install requests
import json  # for handling json data --> pip install json

import os

os.system('cls')


def re_green(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"


root = Tk()

root.title("Crypto Portfolio App")
root.iconbitmap(r'logo.ico')

# ------------------------------------ Start of Header Section ------------------------------

Header_Name = Label(root, text="Name", bg="white", font="verdana 8 bold")
Header_Name.grid(row=0, column=0, sticky=N+S+E+W)

Header_Rank = Label(root, text="Rank", bg="silver", font="verdana 8 bold")
Header_Rank.grid(row=0, column=1, sticky=N+S+E+W)

Header_CurrentPrice = Label(root, text="Current Price", bg="white", font="verdana 8 bold")
Header_CurrentPrice.grid(row=0, column=2, sticky=N+S+E+W)

Header_PricePaid = Label(root, text="Price Paid", bg="silver", font="verdana 8 bold")
Header_PricePaid.grid(row=0, column=3, sticky=N+S+E+W)

Header_PLPer = Label(root, text="Profit/Loss Per", bg="white", font="verdana 8 bold")
Header_PLPer.grid(row=0, column=4, sticky=N+S+E+W)

Header_OneHourChange = Label(root, text="1-Hour Change", bg="silver", font="verdana 8 bold")
Header_OneHourChange.grid(row=0, column=5, sticky=N+S+E+W)

Header_TfHourChange = Label(root, text="24-Hour Change", bg="white", font="verdana 8 bold")
Header_TfHourChange.grid(row=0, column=6, sticky=N+S+E+W)

Header_SevenDayChange = Label(root, text="7-Day Change", bg="silver", font="verdana 8 bold")
Header_SevenDayChange.grid(row=0, column=7, sticky=N+S+E+W)

Header_CurrentValue = Label(root, text="Current Value", bg="white", font="verdana 8 bold")
Header_CurrentValue.grid(row=0, column=8, sticky=N+S+E+W)

Header_PLTotal = Label(root, text="Profit/Loss Total", bg="silver", font="verdana 8 bold")
Header_PLTotal.grid(row=0, column=9, sticky=N+S+E+W)

# ------------------------------------ End of Header Section ------------------------------


def lookup():
    url = 'https://api.nomics.com/v1/currencies/ticker?key=a2bd8a14327d4beac4a8fa484ddd000b52b7c8de&' \
          'ids=BTC,ETH,XRP,NEWO&interval=1h,1d,7d'

    api_response: any = []

    try:
        api_request = requests.get(url)
        api_response = json.loads(api_request.content)
    except Exception as e:
        print(e)

    my_portfolio = [
        {
            "symbol": "BTC",
            "amount_owned": 5,
            "price_paid_per": 2.00
        },
        {
            "symbol": "ETH",
            "amount_owned": 10,
            "price_paid_per": 1.5
        },
        {
            "symbol": "NEWO",
            "amount_owned": 1000000,
            "price_paid_per": 0.00
        }
    ]

    profile_profit_loss: float = 0
    row_count = 1
    total_current_values = 0
    profit_loss = 0
    pie = []
    pie_sizes = []
    for rate in api_response:
        # print(rate)
        for coin in my_portfolio:
            # print(f"{coin['symbol']} =  {rate['id']}")
            # print(f"{float(rate['1h']['price_change_pct'])}")
            if coin['symbol'] == rate['id']:

                total_paid = float(coin['amount_owned']) * float(coin['price_paid_per'])
                current_value = float(coin['amount_owned']) * float(rate['price'])
                profit_loss = current_value - total_paid
                profile_profit_loss += profit_loss
                profit_loss_per_coin = float(rate['price']) - float(coin['price_paid_per'])
                total_current_values += current_value

                pie.append(rate['name'])
                pie_sizes.append(coin['amount_owned'])

                # print(rate['name'])
                # print("Current Price = ${0:.2f}".format(float(rate['price'])))
                # print("Profit/Loss per coin = ${0:.2f}".format(float(profit_loss_per_coin)))
                # print("rank = ${0:.2f}".format(float(rate['rank'])))
                # print("Total Paid = ${0:.2f}".format(float(total_paid)))
                # print("Current Value = ${0:.2f}".format(float(current_value)))
                # print("Total Paid = ${0:.2f}".format(float(total_paid)))
                # print("Profit/ Loss = ${0:.2f}".format(float(profit_loss)))

                name = Label(root, text=rate['name'], bg="white")
                name.grid(row=row_count, column=0, sticky=N + S + E + W)

                rank = Label(root, text=rate['rank'], bg="silver")
                rank.grid(row=row_count, column=1, sticky=N + S + E + W)

                current_price = Label(root, text="${0:.2f}".format(float(rate['price'])), bg="white")
                current_price.grid(row=row_count, column=2, sticky=N + S + E + W)

                price_paid = Label(root, text="${0:.2f}".format(float(coin['price_paid_per'])), bg="silver")
                price_paid.grid(row=row_count, column=3, sticky=N + S + E + W)

                pl_per = Label(root, text="${0:.2f}".format(float(profit_loss_per_coin)), bg="white",
                               fg=re_green(float(profit_loss_per_coin)))
                pl_per.grid(row=row_count, column=4, sticky=N + S + E + W)

                one_hour_change = Label(root, text="{0:.2f}%".format(float(rate['1h']['price_change_pct'])),
                                        bg="silver", fg=re_green(float(rate['1h']['price_change_pct'])))
                one_hour_change.grid(row=row_count, column=5, sticky=N + S + E + W)

                tf_hour_change = Label(root, text="{0:.2f}%".format(float(rate['1d']['price_change_pct'])), bg="white",
                                       fg=re_green(float(rate['1d']['price_change_pct'])))
                tf_hour_change.grid(row=row_count, column=6, sticky=N + S + E + W)

                seven_day_change = Label(root, text="{0:.2f}%".format(float(rate['7d']['price_change_pct'])),
                                         bg="silver", fg=re_green(float(rate['7d']['price_change_pct'])))
                seven_day_change.grid(row=row_count, column=7, sticky=N + S + E + W)

                current_value = Label(root, text="${0:.2f}".format(float(current_value)), bg="white")
                current_value.grid(row=row_count, column=8, sticky=N + S + E + W)

                pl_total = Label(root, text="${0:.2f}".format(float(profit_loss)), bg="silver",
                                 fg=re_green(float(profit_loss)))
                pl_total.grid(row=row_count, column=9, sticky=N + S + E + W)

                row_count += 1

        profile_profits = Label(root, text="P/L: ${0:.2f}".format(float(profit_loss)),
                                fg=re_green(float(profit_loss)), font="verdana 8 bold")
        profile_profits.grid(row=row_count, column=0, sticky=W, padx=10, pady=10)

        root.title("Crypto Portfolio App - Portfolio Value : ${0:.2f}".format(float(total_current_values)))

        api = ""
        update_button = Button(root, text="Update Price", command=lookup)
        update_button.grid(row=row_count, column=9)

        pie_chart_button = Button(root, text="Show Pie Chart", command=lambda: pie_chart(pie, pie_sizes))
        pie_chart_button.grid(row=row_count, column=8)


def pie_chart(labels, sizes):
    # print("pie here")
    # labels = pie
    # sizes = pie
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red']
    patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()


lookup()
root.mainloop()
