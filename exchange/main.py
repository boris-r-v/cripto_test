from poloniex import EPoloniex
from yobit import EYobit
from lbank import  ELbank
from blockchain import EBlockchain
from binance import EBinance
def main():
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

    print(ey.get_url(), ey.bidask)
    print(po.get_url(), po.bidask)
    print(lb.get_url(), lb.bidask)
    print(bc.get_url(), bc.bidask)
    print(bi.get_url(), bi.bidask)

if __name__=='__main__':
    main()