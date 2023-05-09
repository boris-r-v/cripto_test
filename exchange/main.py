import time

from poloniex import EPoloniex
from yobit import EYobit
from lbank import  ELbank
from blockchain import EBlockchain
from binance import EBinance

def periodic():
    ey = EYobit()
    ey.get_bigask(coin1='btc')
#    ey.get_bigask(coin1='eth')

    po = EPoloniex()
    po.get_bigask(coin1='btc')
#    po.get_bigask(coin1='eth')

    lb = ELbank()
    lb.get_bigask(coin1='btc')
#    lb.get_bigask(coin1='eth')

    bc = EBlockchain()
    bc.get_bigask(coin1='btc')
#    bc.get_bigask(coin1='eth')

    bi = EBinance()
    bi.get_bigask(coin1='btc')
#    bi.get_bigask(coin1='eth')

#    print(ey.get_url(), ey.bidask)
#    print(po.get_url(), po.bidask)
#    print(lb.get_url(), lb.bidask)
#    print(bc.get_url(), bc.bidask)
#    print(bi.get_url(), bi.bidask)
    lds = list()
    lds.append(ey)
    lds.append(po)
    lds.append(lb)
    lds.append(bc)

    for l in lds:
        print( bi.get_url(), ' : ', l.get_url(), " : ","bigs", round(100*(float(l.bidask['btc_usdt']['bids'][0][0])-float(bi.bidask['btc_usdt']['bids'][0][0]))/float(bi.bidask['btc_usdt']['bids'][0][0]), 2), "asks", round(100*(float(l.bidask['btc_usdt']['asks'][0][0])-float(bi.bidask['btc_usdt']['asks'][0][0]))/float(bi.bidask['btc_usdt']['asks'][0][0]), 2) )

if __name__=='__main__':
    while(True):
        periodic()
        time.sleep(1)