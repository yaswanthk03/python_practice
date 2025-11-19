import threading
import time
import requests

def web_scraping(url):
    start = time.time()
    try:
        request = requests.get(url)
    except Exception as e:
        print(str(e))
    end = time.time()
    print(f"{threading.current_thread().name} has completed web scrapping in {(end - start):.2f}s")

def arithmetic_operation():
    start = time.time()
    count = 0
    for i in range(1000_000_00):
        count += 1
    end = time.time()
    print(f"{threading.current_thread().name} has completed counting in {(end - start):.2f}s")

def compare_for_best_use_case():
    start_1 = time.time()

    web_scraping_worker_1 = threading.Thread(target=web_scraping, args=('https://books.toscrape.com/index.html',), name='web_scraping_worker_1')
    web_scraping_worker_2 = threading.Thread(target=web_scraping, args=('https://books.toscrape.com/index.html',), name='web_scraping_worker_2')

    web_scraping_worker_1.start()
    web_scraping_worker_2.start()

    web_scraping_worker_1.join()
    web_scraping_worker_2.join()

    end_1 = time.time()

    start_2 = time.time()
    web_scraping('https://books.toscrape.com/index.html')
    web_scraping('https://books.toscrape.com/index.html')
    end_2 = time.time()

    print(f"✅Web Scrapping time using multithreading {(end_1 - start_1):.2f}s vs using single thread {(end_2 - start_2):.2f}s")

def compare_for_worst_use_case():
    start_1 = time.time()

    arithmetic_operation_worker_1 = threading.Thread(target=arithmetic_operation, name='arithmetic_operation_worker_1')
    arithmetic_operation_worker_2 = threading.Thread(target=arithmetic_operation, name='arithmetic_operation_worker_2')

    arithmetic_operation_worker_1.start()
    arithmetic_operation_worker_2.start()

    arithmetic_operation_worker_1.join()
    arithmetic_operation_worker_2.join()

    end_1 = time.time()

    start_2 = time.time()
    arithmetic_operation()
    arithmetic_operation()
    end_2 = time.time()

    print(f"✅Arithmetic Operations time using multithreading {(end_1 - start_1):.2f}s vs using single thread {(end_2 - start_2):.2f}s")


if __name__ == '__main__':
    compare_for_best_use_case()
    compare_for_worst_use_case()