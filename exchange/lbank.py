import iface
import requests

class ELbank(iface.EIface):
    def __init__(self):
        super().__init__()
    def get_url(self):
        return "https://www.lbank.com/"
    def get_bigask(self, coin1='btc', coin2='usdt', limit=3):
        response = requests.get(url=f"https://api.lbkex.com/v2/depth.do?symbol={coin1}_{coin2}&size={limit}")
        self.bidask.update({coin1+'_'+coin2: response.json()['data']})

