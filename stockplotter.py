#!/usr/bin/env python3

import yahoo_fin.stock_info as si
import requests
import matplotlib.pyplot as plt
import ipywidgets

# Getting the actual company name from a ticker symbol
def get_symbol(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)
    result = requests.get(url).json()
    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']

few_days = si.get_data('aapl', start_date = '01/01/2020', end_date = '11/30/2020')

fig,ax = plt.subplots(1,1,figsize=(7,5))
ax.plot(few_days.index, few_days.high)
ax.set_title(get_symbol('AAPL'))
fig.autofmt_xdate()
plt.savefig('apple.png')
