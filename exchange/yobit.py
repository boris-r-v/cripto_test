import iface
import requests

class EYobit(iface.EIface):
    def __init__(self):
        super().__init__()
    def get_bigask(self, coin1='btc', coin2='usdt', limit=3 ):
        response = requests.get(url=f"https://yobit.net/api/3/depth/{coin1}_{coin2}?limit={limit}?ignore_invalid=1?")
        self.bidask.update( response.json() )
    def get_url(self):
        return "https://yobit.net/"