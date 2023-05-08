#https://docs.poloniex.com/?ref=morioh.com&utm_source=morioh.com#authentication-api-signature-generation
import requests

def get_trades(coin1='btc', coin2='usdt'):
    print(f"https://api.poloniex.com/markets/{coin1}_{coin2}/trades")
    response = requests.get(url=f"https://api.poloniex.com/markets/{coin1}_{coin2}/trades")
    return response

def get_price(coin1='btc', coin2='usdt'):
    print(f"https://api.poloniex.com/markets/{coin1}_{coin2}/price")
    response = requests.get(url=f"https://api.poloniex.com/markets/{coin1}_{coin2}/price")
    return response

def main():
#    print( get_trades().json() )
    print(get_price().json())


if __name__=='__main__':
    main()