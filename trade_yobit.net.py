import requests
from config import APP_KEY, APP_SECRET
import time
from urllib.parse import urlencode
import hashlib
import hmac
def get_info():
    values=dict()
    values["method"] = "getInfo"
    values["nonce"] = str(int(time.time()))

    body=urlencode(values).encode('utf-8')
    print(body)
    sign=hmac.new(APP_SECRET.encode('utf-8'), body, hashlib.sha512).hexdigest()
    print(sign)

    headers = {
        "key":APP_KEY,
        "sign": sign
    }

    resource = requests.post(url='https://yobit.net/tapi', headers=headers, data=values)
    return resource

def get_deposit(coin='btc'):
    values=dict()
    values['method']='GetDepositAddress'
    values['coinName']=coin
    values['need_new']=0
    values["nonce"] = str(int(time.time()))
    body=urlencode(values).encode('utf-8')
    print(body)
    sign=hmac.new(APP_SECRET.encode('utf-8'), body, hashlib.sha512).hexdigest()
    print(sign)
    headers = {
        "key":APP_KEY,
        "sign": sign
    }
    resource = requests.post(url='https://yobit.net/tapi', headers=headers, data=values)
    return resource


def main():
    #print( get_info().json() )
    print( get_deposit().json() )

if __name__=='__main__':
    main()