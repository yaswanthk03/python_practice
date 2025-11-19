from multiprocessing import Process
import threading
import time

def work():
    print("Started work..")
    count = 0
    for i in range(1000_000_00):
        count += 1
    print("Work ended..")

if __name__ == '__main__':

    start = time.time()
    w1 = Process(target=work)
    w2 = Process(target=work)

    w1.start()
    w2.start()

    w1.join()
    w2.join()

    end = time.time()
    print(f"{end - start:.2f}") #5.23

    start = time.time()
    t1 = threading.Thread(target=work)
    t2 = threading.Thread(target=work)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.time()
    print(f"{end - start:.2f}") #7.34
    