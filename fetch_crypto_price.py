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

#---------------------------------------------------------
#  Fetch Current market price of Crypto from CoinMarketCap
#  You can get the CoinMarket API Key from your developer account:
#  https://pro.coinmarketcap.com/account
#  Refer to the API documentation here: https://coinmarketcap.com/api/
#---------------------------------------------------------

class CryptoPrice:
    def __init__(self, currency='USD'):
        self.currency = currency
        self.base_url = r'https://pro-api.coinmarketcap.com/v1/cryptocurrency'        
    
    #-------------------------------------------------
    #   Fetch Current Market Price of a crypto
    #-------------------------------------------------
    def get_current_price(self, token):
        url = f"{self.base_url}/quotes/latest"
    
        header = {}
        header['X-CMC_PRO_API_KEY'] = settings.API_KEY
        header['Accepts'] = 'application/json'

        data = {}
        data['symbol'] = token
        data['convert'] = self.currency

        response = requests.get(url, headers=header, params=data, timeout=10)

        crypto_info = response.json()

        crypto_price = crypto_info['data'][token]['quote'][self.currency]['price']

        #print(json.dumps(crypto_info, indent=4))
        #print(crypto_price)

        return crypto_price


    #---------------------------------------------------------
    #  Fetch Current market price of Multiple Crypto from CoinMarketCap
    #---------------------------------------------------------    
    def get_current_price_multiple(self, token_list):

        crypto_price = {}
        url = f"{self.base_url}/quotes/latest"
    
        header = {}
        header['X-CMC_PRO_API_KEY'] = settings.API_KEY
        header['Accepts'] = 'application/json'

        symbols = ",".join(token_list)

        data = {}
        data['symbol'] = symbols
        data['convert'] = self.currency

        response = requests.get(url, headers=header, params=data, timeout=10)

        crypto_info = response.json()

        for token in token_list:
            crypto_price[token] = crypto_info['data'][token]['quote'][self.currency]['price']

        #print(json.dumps(crypto_info, indent=4))
        #print(crypto_price)

        return crypto_price



def main():
    obj = CryptoPrice()

    token = ['BTC','ETH', 'XRP', 'DOGE']
    token = 'BTC'
    price = obj.get_current_price(token)

    token_list = ['BTC','ETH', 'XRP', 'DOGE']
    crypto_price = obj.get_current_price_multiple(token_list)

    #print(price)
    print(crypto_price)
   
    
if __name__ == '__main__':
    main()
    print("Done")