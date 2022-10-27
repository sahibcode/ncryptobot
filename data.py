import pandas as pd
from binance.client import Client
import datetime as dt
import csv

# Use this file to get data of all binance futures symbols at once for a specific timeframe since 1 Jan 2020
# use not mark data, use the simple k-line usd m futures data for futures trading
# only defualt timeframes are available, and mostly data before 1 Jan 2020 is not available, so
# confirm from binance before putting date of before 2020



api_key = 'APIKEY'
api_secret = 'SECRETKEY'
client = Client(api_key, api_secret)


with open('data.csv', newline='') as f:     # read symbols csv and convert to list
    reader = csv.reader(f)
    symbols_data = list(reader)


new_data = [val for sublist in symbols_data for val in sublist]     # removing nested list, only keeping simple symbol list


number = 1
for s in new_data:
    print(s)
    klines = client.futures_historical_klines(s, '5m', '1 Jan, 2020')
    data = pd.DataFrame(klines)
    data.columns = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'qav', 'num_trades',
                    'taker_base_vol', 'taker_quote_vol', 'ignore']
    data.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in data.close_time]
    data.to_csv(s + '.csv', index=None, header=True)

    print('\nAmount of symbols downloaded : ', number)
    number += 1


