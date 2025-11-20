import asyncio
import aiohttp
import time


async def fetch(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            print("Status: ", response.status)
            print("Content-Type: ", response.headers['content-type'])
            if response.headers['content-type'] == 'text/html':
                content = await response.text()
                print(content)

start1 = time.time()            
asyncio.run(fetch('https://books.toscrape.com/'))
end1 = time.time()
print(f'{(end1 - start1):.2f}')

async def multiple_fetches():
    start1 = time.time()   
    arr = [fetch('https://books.toscrape.com/') for _ in range(1000)]
    await asyncio.gather(*arr)
    end1 = time.time()
    print(f'{(end1 - start1):.2f}')

asyncio.run(multiple_fetches())
