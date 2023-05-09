class EIface():
    def __init__(self):
        self.bidask = {'btc_usdt':{}}
    def get_bigask(self, coin1='btc', coin2='usdt', limit=3):
        raise NotImplementedError('override EIface.get_bidask')
    def get_url(self):
        raise NotImplementedError('override EIface.get_url')
