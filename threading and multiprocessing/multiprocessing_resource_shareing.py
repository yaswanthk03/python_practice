from multiprocessing import Process, Queue, Value, Array, current_process as cp
import time

def value_example(counter):
    for i in range(5):
        time.sleep(0.1)
        with counter.get_lock():
            counter.value += 1
            print(f"value = {counter.value}, process name - {cp().name}")

def queue_example(q):
    for i in range(5):
        time.sleep(0.1)
        if not q.empty():
            print(f'Queue item {q.get()} removed, Process name - {cp().name}')
        q.put(f'{cp().name}_{str(i)}')
    

if __name__ == '__main__':
    
    counter = Value('i', 0)
    q = Queue(10)
    
    # w1 = Process(target=value_example, args=(counter, ), name='w1')
    # w2 = Process(target=value_example, args=(counter, ), name='w2')

    # w1.start()
    # w2.start()

    # w1.join()
    # w2.join()
    # print(f"Final value {counter.value}")
    
    w1 = Process(target=queue_example, args=(q, ), name='w1')
    w2 = Process(target=queue_example, args=(q, ), name='w2')

    w1.start()
    w2.start()

    w1.join()
    w2.join()
    
    