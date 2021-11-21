from STLB100_GATT_client import run_ble_client
import sys
import time
import datetime
import platform
import asyncio

async def run():
    queue = asyncio.Queue()

    client_task = run_ble_client(queue)
    consumer_task = run_ble_consumer(queue)
    await asyncio.gather(client_task, consumer_task)

    print('asyncio run() done')

async def run_ble_consumer(queue: asyncio.Queue):
    while True:
        # Use await asyncio.wait_for(queue.get(), timeout=1.0) if you want a timeout for getting data.
        epoch, data = await queue.get()
        if data is None:
            print("BLE disconnecting! Exiting consumer loop...")
            break
        else:
            timestamp = datetime.datetime.fromtimestamp(epoch/1000.)
            print(f"{data}: {timestamp}")

if __name__ == "__main__":
   
    asyncio.run(run())
