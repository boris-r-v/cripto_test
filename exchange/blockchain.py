import iface
import requests

class EBlockchain(iface.EIface):
    def __init__(self):
        super().__init__()
    def get_url(self):
        return "https://api.blockchain.com/"
    def get_bigask(self, coin1='btc', coin2='usdt', limit=3 ):
        response = requests.get(url=f"https://api.blockchain.com/v3/exchange/l2/{coin1.upper()}-{coin2.upper()}")
        asks = list()
        for i in range(0, limit):
            asks.append( [response.json()['asks'][i]['px'], response.json()['asks'][i]['qty']] )
        bids = list()
        for i in range(0, limit):
            bids.append([response.json()['bids'][i]['px'], response.json()['bids'][i]['qty']])
        self.bidask.update({coin1+'_'+coin2: {"asks":asks, "bids": bids}})
