import asyncio
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def worker(num):
    print('Started work ...', threading.current_thread().name)
    time.sleep(1)
    print('Task ended.', threading.current_thread().name)
    return num

async def main():
    loop = asyncio.get_running_loop()
    start = time.time()
    with ThreadPoolExecutor(max_workers=5, thread_name_prefix='w') as pool:   
        tasks = [
            loop.run_in_executor(pool, worker, i)
            for i in range(10)
        ]
        result = await asyncio.gather(*tasks)
        print('result:', result)
    end = time.time()
    print(f'Time taken: {end - start:.2f}s')
asyncio.run(main())