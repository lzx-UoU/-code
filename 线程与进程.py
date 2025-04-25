"""
多线程(线程是计算机可以被CPU调度的最小单元,即真正在工作的.)

1.守护与非守护线程

import time
import threading

def worker(message):
    for i in range(5):
        res = message - i
        print(f'{res}')
        time.sleep(1)

daemon_thread = threading.Thread(target = worker,args = (10,),daemon = True)
daemon_thread.start()             #守护线程:依赖主线程,主线程结束时被强制终止,不会阻塞程序退出(使用场景:生命周期依赖主线程,比如后台任务)

not_daemon_thread = threading.Thread(target = worker,args = (10,),daemon = False)
#not_daemon_thread.start()        #非守护线程:独立于主线程,完成任务后才结束,会阻塞程序退出,直到所有非守护线程完成(使用场景:生命周期独立于主线程,适合需要完整执行的任务)

time.sleep(2)
print("主线程结束")


2.回调函数

#用于处理线程完成后的结果
import threading

def task():
    print("任务执行中")
    return "任务完成"

def callback(result):
    print("回调函数收到结果:", result)

thread = threading.Thread(target=task)
thread.start()
thread.join()
callback("任务完成")


#用于实现观察者模式
class Subject:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer(message)

def observer1(message):
    print(f"观察者1收到消息：{message}")

def observer2(message):
    print(f"观察者2收到消息：{message}")

subject = Subject()
subject.register_observer(observer1)
subject.register_observer(observer2)

subject.notify_observers("状态发生变化")


3.单例模式

import threading

class Singleton(object):

    instance = None

    lock = threading.RLock()

    def __init__(self):

        pass

    def __new__(cls,*args,**kw):

        if cls.instance: return cls.instance

        with cls.lock:

            if cls.instance:

                return cls.instance

            cls.instance = super().__new__(cls)

            return cls.instance


4.线程池与闭包函数

from concurrent.futures import ThreadPoolExecutor

def outer(x):

    def inner(y):

        return x * y

    return inner

with ThreadPoolExecutor(3) as executor:

    futures = [executor.submit(outer,x) for x in range(5)]

    for future in futures:

        print(future.result()(10))    #获取结果(当调用 future.result() 时,主线程会卡在这一行代码处,直到任务执行完毕并返回结果)

闭包函数在并发编程中的作用:
1. 捕获外部变量并传递给线程闭包可以捕获外部函数的变量,并将这些变量作为上下文传递给线程任务,这在需要为多个线程动态生成不同参数的任务时非常有用.
2. 动态生成任务闭包可以动态生成带有不同逻辑或参数的任务,适合在并发编程中处理大量类似的任务.


5.线程安全:线程安全是指算法或程序在多个线程同时执行期间能够正常运行的属性,如果代码在多线程环境中运行时具有确定性行为并生成所需的输出,则认为代码是线程安全的
1.共享的可变数据:线程共享其父进程的内存,因此所有变量和数据结构都在线程之间共享,这可能会导致在处理共享的可更改数据时出现错误
2.非原子作:当涉及多个步骤的作被上下文切换中断时,这些操作发生在多线程环境中,如果在操作期间切换线程,这可能会导致意外结果

import threading
import time
from concurrent.futures import ThreadPoolExecutor

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.account_Rlock = threading.RLock()

    def withdraw(self, amount):
        with self.account_Rlock:
            if self.balance >= amount:
                new_balance = self.balance - amount
                print(f"Withdrawing {amount}...")
                time.sleep(0.1)  # Simulate a delay
                self.balance = new_balance
            else:
                raise ValueError("Insufficient balance")

    def deposit(self, amount):
        with self.account_Rlock:
            new_balance = self.balance + amount
            print(f"Depositing {amount}...")
            time.sleep(0.1)  # Simulate a delay
            self.balance = new_balance

account = BankAccount(1000)

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(account.withdraw, 700)
    executor.submit(account.deposit, 1000)
    executor.submit(account.withdraw, 300)

print(f"Final account balance: {account.balance}")




多进程(进程是计算机资源分配的最小单元,一个进程可以有多个线程,同一个进程中的线程可以共享同一个进程的资源)

1.进程间的数据共享(每个进程都有自己的独立内存空间,进程间无法直接访问彼此的内存,因此需要通过特定的机制来实现数据共享)
from multiprocessing import Process, Manager

def worker(shared_dict, shared_list):
    shared_dict[1] = '1'
    shared_dict['2'] = 2
    shared_list.reverse()

if __name__ == "__main__":
    with Manager() as manager:
        shared_dict = manager.dict()
        shared_list = manager.list(range(10))

        p = Process(target=worker, args=(shared_dict, shared_list))
        p.start()
        p.join()

        print("共享字典：", shared_dict)
        print("共享列表：", shared_list)


2.进程安全
import time
import multiprocessing

lock_object = multiprocessing.RLock()

def func(lock_object):
    with lock_object:
        print("我是主进程,我正在被执行!")
        time.sleep(1)

if __name__ == "__main__":

    for _ in range(3):
        t = multiprocessing.Process(target = func,args = (lock_object,))
        t.start()


使用信号量限制访问
1.当资源数量有限并且许多线程尝试访问这些有限的资源时,它使用计数器来限制多个线程对关键部分的访问,构造函数接受一个参数,该参数表示获取该参数的最大并发线程数
2.每次调用都会将信号量的计数器减少1,当计数器达到零时,进一步的调用将被阻止

import random
import threading
import time
import datetime
from concurrent.futures import ThreadPoolExecutor


teller_semaphore = threading.Semaphore(2)

def now():
    return datetime.datetime.now()

def serve_customer(name):
    print(f"{now()}: {name} is waiting for a teller.")
    with teller_semaphore:
        print(f"{now()}: {name} is being served by a teller.")
        time.sleep(random.randint(1, 3))
        print(f"{now()}: {name} is done being served.")

customers = [
    "Customer 1",
    "Customer 2",
    "Customer 3",
]

with ThreadPoolExecutor(3) as executor:
    for customer_name in customers:
        thread = executor.submit(serve_customer, customer_name)

print(f"{now()}: All customers have been served.")
"""
