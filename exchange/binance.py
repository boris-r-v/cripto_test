import iface
import requests

class EBinance(iface.EIface):
    def __init__(self):
        super().__init__()
    def get_url(self):
        #https://api1.binance.com/api/v3/depth?symbol=BTCUSDT&limit=2
        return "https://binance.com"

    def get_bigask(self, coin1, coin2, limit=1 ):
        response = requests.get(url=f"https://api1.binance.com/api/v3/depth?symbol={coin1.upper()}{coin2.upper()}&limit={limit}")
        if ( "msg" not in response.json() ):
            self.bidask.update({coin1+'_'+coin2: {"asks":response.json()['asks'], "bids": response.json()['bids']}})
        else:
            print(response.json())
            print(f"{response.json()['msg']}: {coin1.upper()}-{coin2.upper()}")
