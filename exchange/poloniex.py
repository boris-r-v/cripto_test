import iface
import requests

class EPoloniex(iface.EIface):
    def __init__(self):
        super().__init__()
    def get_url(self):
        return "https://poloniex.com/"
    def get_bigask(self, coin1='btc', coin2='usdt', limit=3):
        response = requests.get(url=f"https://api.poloniex.com/markets/{coin1}_{coin2}/orderBook")
        asks = list()
        for i in range(0, limit):
            asks.append( [response.json()['asks'][2*i], response.json()['asks'][2*i+1]] )
        bids = list()
        for i in range(0, limit):
            bids.append( [response.json()['bids'][2*i], response.json()['bids'][2*i+1]] )
        self.bidask.update({coin1+'_'+coin2: {"asks":asks, "bids": bids}})

