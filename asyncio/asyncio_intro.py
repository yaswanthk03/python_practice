import asyncio
import time
import threading

async def fetch_url():
    print(f'Fetching using - {threading.current_thread().name}')
    await asyncio.sleep(2) # Non blocking function. (time.sleep is a blocking function.)
    print(f'Fetch complete.')

async def main():
    await asyncio.gather(fetch_url(), fetch_url(), fetch_url())
    


if __name__ == '__main__':
    start1 = time.time()
    asyncio.run(fetch_url())
    end1 = time.time()
    start2 = time.time()
    asyncio.run(main())
    end2 = time.time()

    print(f'\nTime for one request = {end1 - start1:.2f}, For 3 requests = {end2 - start2:.2f}')
    