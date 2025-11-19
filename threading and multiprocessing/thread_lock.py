import threading
from concurrent.futures import ThreadPoolExecutor
import time

class BankAccount():
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount:int):
        time.sleep(0.2)
        self.balance += amount
        print(f"Amount of {amount} deposited to account - {threading.current_thread().name}")
    
    def withdraw(self, amount:int):
        if self.balance >= amount:
            time.sleep(0.2)
            self.balance -= amount
            print(f"Amount of {amount} withdrawn from account - {threading.current_thread().name}")
        else:
            print("No sufficient balance -", threading.current_thread().name)


# account = BankAccount(1000)
# with ThreadPoolExecutor(max_workers=3, thread_name_prefix="worker") as executor:
#     executor.submit(account.withdraw, 500)
#     executor.submit(account.withdraw, 700)
#     executor.submit(account.deposit, 1000)
#     executor.submit(account.withdraw, 300)
    
    # Inference:
    #     expected out put:
    #         Amount of 500 withdrawn from account - worker_0            
    #         No sufficient balance - worker_1
    #         Amount of 1000 deposited to account - worker_0
    #         Amount of 300 withdrawn from account - worker_1
    
    #     Out put due to no thread safety:
    #         Amount of 700 withdrawn from account - worker_1
    #         Amount of 500 withdrawn from account - worker_0
    #         No sufficient balance - worker_1
    #         Amount of 1000 deposited to account - worker_2

class BankAccountWithThreadSafety():
    def __init__(self, balance=0):
        self.balance = balance
        self.account_lock = threading.Lock()

    def deposit(self, amount:int):
        with self.account_lock:
            time.sleep(0.2)
            self.balance += amount
            print(f"Amount of {amount} deposited to account - {threading.current_thread().name}")
    
    def withdraw(self, amount:int):
        with self.account_lock:
            if self.balance >= amount:
                time.sleep(0.2)
                self.balance -= amount
                print(f"Amount of {amount} withdrawn from account - {threading.current_thread().name}")
            else:
                print("No sufficient balance -", threading.current_thread().name)

account = BankAccountWithThreadSafety(1000)
with ThreadPoolExecutor(max_workers=3, thread_name_prefix="worker") as executor:
    executor.submit(account.withdraw, 500)
    executor.submit(account.withdraw, 700)
    executor.submit(account.deposit, 1000)
    executor.submit(account.withdraw, 300)

    # OutPut:
    #     Amount of 500 withdrawn from account - worker_0
    #     No sufficient balance - worker_1
    #     Amount of 1000 deposited to account - worker_2
    #     Amount of 300 withdrawn from account - worker_0