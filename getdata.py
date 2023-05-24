import pandas as pd
from binance.client import Client
import datetime as dt


# Use this file to get binance futures symbol data for different timeframe
# please first do pip install for pandas, python-binance, datetime
# use not mark data, use the simple k-line usd m futures data for futures trading
# only defualt timeframes are available, and usually data before 1 Jan 2020 is not available, so
# confirm from binance before putting date of before 2020



api_key = 'YOURAPI'
api_secret = 'YOURSECRET'
client = Client(api_key, api_secret)


symbol = input('\nType Symbol name, like BTCUSDT : ')
interval = input('\nType Timeframe, like 15m or 1 m : ')
since = input('\nType How much time of Data you want, like since 1 Jan, 2020 : ')

print("\nDownloading Data")

klines = client.futures_historical_klines(symbol, interval, since)


print("Converting to CSV")
data = pd.DataFrame(klines)
data.columns = ['open_time','open', 'high', 'low', 'close', 'volume','close_time', 'qav','num_trades','taker_base_vol','taker_quote_vol', 'ignore']
data.index = [dt.datetime.fromtimestamp(x/1000.0) for x in data.close_time]
data.to_csv(symbol+'.csv', index = None, header=True)



# convert time in data to normal time from milliseconds of binance
# df['open_time'] = pd.to_datetime(df['open_time'], unit='ms').dt.tz_localize('UTC').dt.tz_convert('Asia/Karachi')
