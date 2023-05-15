import json
import websockets
import asyncio

async def main():
    url='wss://stream.binance.com:9443/stream?streams=btcusdt@trade'
    async with websockets.connect(url) as client:
        while True:
            print(await client.recv())
            #data = json.load(await client.recv())['data']
            #print(data['E'], '->', data['c'])


if __name__=='__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
