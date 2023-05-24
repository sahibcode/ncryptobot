import pandas as pd

''' This script will take OHLCV data csv file and calculate vwap and vwap std dev bands 1 & 2
and output you a new csv file of the previous file but with VWAP Data. You can download OHLCV data with getdata.py
 for a single file of any timeframe'''



# Load data from csv file
df = pd.read_csv('yourfilename.csv')

# Calculate typical price
df['typical_price'] = (df['high'] + df['low'] + df['close']) / 3

# Convert open_time column to datetime and extract the date
df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')  # convert from milliseconds
df['date'] = df['open_time'].dt.date  # extract the date

# Calculate VWAP
df['vwap'] = df.groupby(df['date'])['typical_price'].transform(lambda x: (x * df.loc[x.index, 'volume']).cumsum() / df.loc[x.index, 'volume'].cumsum())

# Calculate 1 & 2 stdev
df['vwap_stdev'] = df.groupby('date')['vwap'].transform(lambda x: x.std())      # calculates stdev of vwap, this is not stdev bands
# creating 1 stdev upper & lower band
df['vwap_upperband1'] = df['vwap'] + df['vwap_stdev']
df['vwap_lowerband1'] = df['vwap'] - df['vwap_stdev']
# creating 2 stdev upper & lower band
df['vwap_upperband2'] = df['vwap'] + 2 * df['vwap_stdev']
df['vwap_lowerband2'] = df['vwap'] - 2 * df['vwap_stdev']


