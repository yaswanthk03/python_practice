import asyncio
import os
import time
from concurrent.futures import ProcessPoolExecutor
import math

def cpu_heavy(n):
    print(f'[process] PID = {os.getpid()}, computing {n}')
    total = 0
    for i in range(10_000_000):
        total += math.sqrt(i)
    return n

async def main():
    loop = asyncio.get_running_loop()
    start = time.time()
    with ProcessPoolExecutor(max_workers=2) as pool:   
        tasks = [
            loop.run_in_executor(pool, cpu_heavy, i)
            for i in range(10)
        ]
        result = await asyncio.gather(*tasks)
        print('Process result:', result)
    end = time.time()
    print(f'Time taken: {end - start:.2f}s')

if __name__ == '__main__':
    asyncio.run(main())