import iface
import requests

class EBinance(iface.EIface):
    def __init__(self):
        super().__init__()
    def get_url(self):
        #https://api1.binance.com/api/v3/depth?symbol=BTCUSDT&limit=2
        return "https://binance.com"
    def get_bigask(self, coin1='btc', coin2='usdt', limit=3 ):
        response = requests.get(url=f"https://api1.binance.com/api/v3/depth?symbol={coin1.upper()}{coin2.upper()}&limit={limit}")
        self.bidask.update({coin1+'_'+coin2: {"asks":response.json()['asks'], "bids": response.json()['bids']}})
