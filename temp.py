#-------------------------------------------------------------------------------
# Name      :   fetch_crypto_price.py
# Purpose   :   This Python script takes crypto tokens and 
#               fetch OHLC data via CoinMarketCap in Python
# Author    :   Kiran Chandrashekhar
# Webste    :   https://sapnaedu.com
# Created   :   26-Dec-2022
#-------------------------------------------------------------------------------

import conf as settings
import requests
import json

#-----------------------------------------------------------
#  Fetch Current market price of Crypto from CoinMarketCap
#-----------------------------------------------------------

def get_current_price(token:str, currency:str)->float:
    url = r"https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"

    header = {}
    header['X-CMC_PRO_API_KEY'] = settings.API_KEY
    header['Content-Type'] = 'application/json'

    data = {}
    data['symbol'] = token
    data['convert'] = currency

    response = requests.get(url, headers=header, params=data)

    crypto_info = response.json()
    #print(json.dumps(crypto_info, indent=4))
    return crypto_info


token = 'BTC,ETH,XRP'
currency = 'USD'
crypto_info = get_current_price(token, currency)
#print(json.dumps(crypto_info, indent=4))

bitcoin_price   = crypto_info['data']['BTC'][0]['quote'][currency]['price']
ethereum_price  = crypto_info['data']['ETH'][0]['quote'][currency]['price']
ripple_price    = crypto_info['data']['XRP'][0]['quote'][currency]['price']

print(bitcoin_price)
print(ethereum_price)
print(ripple_price)

