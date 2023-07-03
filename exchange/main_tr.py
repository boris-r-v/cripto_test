import time
import datetime

from binance import EBinance
jcs = {"price":0, "volume":1}   #aka json schema

def update( st ):
    st.get_bigask(coin1='eth', coin2='btc', limit=1)
    st.get_bigask(coin1='ltc', coin2='btc', limit=1)
    st.get_bigask(coin1='ltc', coin2='eth', limit=1)
    st.get_bigask(coin1='bnb', coin2='eth', limit=1)

def show( st ):
    for i in st.bidask:
        print( i, st.bidask[i] )
"""
Расчитывает кросс курс
@:param fr какую монету имеем - основание рынка (BTC, ETH, BNB, BUSD)
@:param to какую хотим получить - основание рынка (BTC, ETH, BNB, BUSD)
@:param via через какую монету посчитать кросс-курс
@:param bi хралище данных с биржи
"""
def calculate2 (fr, to, via, stock, fail=False):
    try:
        #print(f"from:{fr}, to:{to}, via:{via}" )
        key1 = via+"_"+fr   #тут цена обратная asks на рынке fr
        key2 = via+"_"+to   #тут цена прямая bids на рынке to
        dkey = fr+"_"+to    #тут цена прямая bids на рынке to
        #print(f"key1:{key1}, key2:{key2}")
        ask1 = float(stock.bidask[key1]["asks"][0][jcs["price"]])
        rask1 = 1 / ask1
        bid2 = float(stock.bidask[key2]["bids"][0][jcs["price"]])
        ret = rask1 * bid2
        #print(f"aks1:{ask1}, rask1:{rask1}, bid:{bid2}, ret: {ret}")
        direct = float(stock.bidask[dkey]["bids"][0][jcs["price"]])
        #print(f"direct:{direct}, ret:{ret}")
        profitGross=100*(ret-direct)/direct
        profitNet = profitGross - 2*0.1
        print (f"from:{fr.upper()} to:{to.upper()} via:{via.upper()} profitGross:{profitGross}, profitNet:{profitNet}")
    except Exception as ex:
        print(ex)
        if (not fail):
            calculate(to, fr, via, stock, True )
        else:
            pass
def calculate (fr, to, via, stock, fail=False):
        #print(f"from:{fr}, to:{to}, via:{via}" )
        key1 = via+"_"+fr   #тут цена обратная asks на рынке fr
        key2 = via+"_"+to   #тут цена прямая bids на рынке to
        dkey = fr+"_"+to    #тут цена прямая bids на рынке to
        #print(f"key1:{key1}, key2:{key2}")
        ask1 = float(stock.bidask[key1]["asks"][0][jcs["price"]])
        rask1 = 1 / ask1
        bid2 = float(stock.bidask[key2]["bids"][0][jcs["price"]])
        ret = rask1 * bid2
        #print(f"aks1:{ask1}, rask1:{rask1}, bid:{bid2}, ret: {ret}")
        direct = 0.0
        try:
            direct = float(stock.bidask[dkey]["bids"][0][jcs["price"]])
        except Exception as ex:
            #print("\tNo way ", ex )
            dkey = to + "_" + fr
            dir = float(stock.bidask[dkey]["asks"][0][jcs["price"]])
            direct = 1 / dir
            #print(f"\tdirect:{direct}, dir:{dir}, way: {dkey}")

        profitGross=100*(ret-direct)/direct
        profitNet = profitGross - 2*0.1
        if ( profitNet > 0):
            print (f"{datetime.datetime.now()} from:{fr.upper()} to:{to.upper()} via:{via.upper()} profitGross:{profitGross}, profitNet:{profitNet}")

if __name__=='__main__':
    bi = EBinance()
    while(True):
        bi.get_bigask(coin1='eth', coin2='btc', limit=1)
        bi.get_bigask(coin1='ltc', coin2='btc', limit=1)
        bi.get_bigask(coin1='bnb', coin2='btc', limit=1)
        bi.get_bigask(coin1='bch', coin2='btc', limit=1)
        bi.get_bigask(coin1='bnb', coin2='eth', limit=1)
        bi.get_bigask(coin1='ltc', coin2='eth', limit=1)
        bi.get_bigask(coin1='eth', coin2='busd', limit=1)
        bi.get_bigask(coin1='btc', coin2='busd', limit=1)
        bi.get_bigask(coin1='ltc', coin2='busd', limit=1)
        bi.get_bigask(coin1='bnb', coin2='busd', limit=1)
        #show(bi)
        calculate(fr='eth', to='btc', via='ltc', stock=bi)
        calculate(fr='btc', to='eth', via='ltc', stock=bi)
        calculate(fr='btc', to='eth', via='bnb', stock=bi)
        calculate(fr='eth', to='btc', via='bnb', stock=bi)
        calculate(fr='eth', to='busd', via='bnb', stock=bi)
        calculate(fr='btc', to='busd', via='bnb', stock=bi)
        calculate(fr='eth', to='busd', via='ltc', stock=bi)
        calculate(fr='btc', to='busd', via='ltc', stock=bi)
        #print("---------------------------")



        time.sleep(1)