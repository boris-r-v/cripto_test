import requests
from datetime import datetime
#https://yobit.net/ru/api/

def get_info():
    response = requests.get(url="https://yobit.net/api/3/info")
#    with open ("info.json", "w") as file:
#        file.write(response.text)
    return response.text

def get_ticket(coin1="btc", coin2='usdt'):
    #response = requests.get (url="https://yobit.net/api/3/trades/ltc_btc?ignore_invalid=1")
    response = requests.get (url=f"https://yobit.net/api/3/ticker/{coin1}_{coin2}?ignore_invalid=1?")
#    with open ("ticket.json", "w") as file:
#        file.write(response.text)
    return response


def get_depth(coin1='btc', coin2='usdt', limit=10):
    response = requests.get (url=f"https://yobit.net/api/3/depth/{coin1}_{coin2}?limit={limit}?ignore_invalid=1?")
#    with open ("depth.json", "w") as file:
#        file.write(response.text)
    return response.text

def get_trades(coin1='btc', coin2='usd', limit=10):
    response = requests.get (url=f"https://yobit.net/api/3/trades/{coin1}_{coin2}?limit={limit}?ignore_invalid=1?")
#    with open ("trades.json", "w") as file:
#        file.write(response.text)
    return response

def parse_ticket( data ):
    for key in data:
        print(f"ticket {key}: {data[key]['last']}, Date: {datetime.fromtimestamp(data[key]['updated'])}")


def parse_trades( data ):
    total_bid_amt=0
    total_ask_amt=0
    ask_price=[0,0] #amount, datetime
    bid_price=[0,0]

    for key in data:
        for row in data[key]:
            #print(row, datetime.fromtimestamp(row['timestamp']))
            if ( row['type'] == 'ask' ):
                total_bid_amt += row['price']*row['amount']
                if ( row['timestamp'] > ask_price[0] ):
                    ask_price[1] = row['price']
                    ask_price[0] = row['timestamp']
            else:
                total_ask_amt += row['price'] * row['amount']
                if (row['timestamp'] > bid_price[0]):
                    bid_price[1] = row['price']
                    bid_price[0] = row['timestamp']

        print(f"{key}\n\t[-] ask amount {round(total_ask_amt,2)} ask_price: {ask_price[1]} time: {datetime.fromtimestamp(ask_price[0])}\n"
              f"\t[+] bid amount {round(total_bid_amt,2)} bid_price: {bid_price[1]} time: {datetime.fromtimestamp(bid_price[0])}")

    #ask — цена покупки, а bid — цена продажи

def main():
    #print(get_info())
    #print (get_ticket(coin2="usd").text )
    #print(get_depth())
    #print(get_trades().text)
    parse_ticket(get_ticket().json())
    parse_trades(get_trades().json())

    #parse_ticket(get_ticket(coin1='eth').json())
    #parse_trades(get_trades(coin1='eth').json())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
#https://jsonviewer.stack.hu/

