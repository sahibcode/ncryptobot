import ccxt
import time

''' This code helps you set leverage amount to any amount you input in, as news traders usually want to quickly enter
in position and setting leverage for every coin is time hassle for them'''



# create the Binance exchange object
exchange = ccxt.binanceusdm({'timeout': 20000})

# connecting to our binance account

exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)

exchange = exchange_class({
        'apiKey': 'YOUR API',
        'secret': 'YOUR SECRET',
        'options': {'defaultType': 'future'},
        'enableRateLimit': True,
    })

print('\nLogin Successful\n')


while True:
    # get a list of all available symbols on Binance
    symbols = exchange.load_markets()

    # iterate over each symbol
    for symbol in symbols:
        # set the leverage to 3
        exchange.set_leverage(3, symbol)

    print('All coins leverage set')
    # wait 5 seconds
    time.sleep(5)
