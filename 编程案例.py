"""
TCP编程案例1(客服服务)
server.py

import socket

def server_socket():

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    sock.bind(("192.168.1.105",8001))

    sock.listen(5)

    while True:

        conn,address = sock.accept()

        conn.sendall("欢迎使用xx系统".encode('utf-8'))

        data = conn.recv(1024)

        if not data or data.decode('UTF-8') == "exit":

            break

        print(f"{data.decode('UTF-8')}")

        conn.sendall("请继续输入你的问题".encode('UTF-8'))

        conn.close()

    sock.close()

def server():

    server_socket()

if __name__ == "__main__":

    server()

client.py

import socket

def client_socket():

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    client.connect(("192.168.1.105",8001))

    print(client.recv(1024).decode('UTF-8'))

    while True:

        message = input("请输入需要咨询本网页的问题(输入exit退出)")

        if message.upper() == b"exit":

            break

        client.sendall(message.encode('UTF-8'))

        print(client.recv(1024).decode('UTF-8'))

    client.close()

def client():

    client_socket()

if __name__ == "__main":

    client()


TCP编程案例2(文件上传)

#server.py

import socket
import struct
import os

def main():

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    sock.bind(("127.0.0.1",8001))

    sock.listen(5)

    try:

        while True:

            conn,address = sock.accept()

            handle_client(conn)

    finally:

        sock.close()

def recv_all(sock,n):      #对于接收数据时可能会出现接收不完全的时候,需要循环接收直到获得指定的字节长度.

    data = bytearray()     #用于创建一个可变字节数组,输出 b''.

    while len(data) < n:

        remaining = n - len(data)

        packet = sock.recv(remaining)

        if not packet:

            raise ConnectionError("connection closed unexpectedly")

        data.extend(packet)    #把接收到的字节长度添加到data中

    return data

def handle_client(conn):      #接收文件信息

    file_name_len = struct.unpack('!I',recv_all(conn,4))[0]   #4字节

    file_name = recv_all(conn,file_name_len).decode('utf-8')

    print(f'Receiving file:{file_name}')

    file_size = struct.unpack('!Q',recv_all(conn,8))[0]    #8字节


    save_dir = 'upload'    #创建保存目录

    os.makedirs(save_dir,exist_ok = True)    #创建文件夹

    file_path = os.path.join(save_dir,file_name)   #拼接目录路径,返回一个拼接后的完整路径.


    received = 0        #初始化接收大小

    with open(file_path,'wb') as f:

        while received < file_size:

            chunk_header = recv_all(conn,4)       #接收块长度(4字节)

            chunk_size = struct.unpack('!I',chunk_header)[0]

            chunk_data = recv_all(conn,chunk_size)   #接收块数据

            f.write(chunk_data)

            received += chunk_size

    print(f'{file_name} received successfully')

    conn.close()

if __name__ == "__main__":

    main()


#client.py

import struct
import os
import socket

def send_all(sock,data):

    sock.sendall(data)

def send_file(file_path,server_address):

    try:

        if not os.path.exists(file_path):

            raise FileExistsError(f"File {file_path} not found")

        file_name = os.path.basename(file_path)

        file_size = os.path.getsize(file_path)

        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:

            sock.connect(server_address)

            file_name_encode = file_name.encode('utf-8')

            send_all(sock,struct.pack('!I',len(file_name_encode)))    #发送文件名长度

            send_all(sock,file_name_encode)

            send_all(sock,struct.pack('!I',file_size))


            sent = 0

            with open(file_path,'rb') as f:    #循环发送文件内容,直到全部发送完成.

                while sent < file_size:

                    chunk = f.read(4096)

                    if not chunk:

                        break

                    send_all(sock,struct.pack('!I',len(chunk)))

                    send_all(sock,chunk)

                    sent += chunk

            print(f'File {file_name} sent successfully')

    except Exception as e:

        print(f'Error:{str(e)}')

if __name__ == "__mian__":

    server_address = ('localhost',8001)

    file_to_send = input('Enter file path to send:  ')

    send_file(file_to_send,server_address)

TCP编程文件上传实现思路:                                 (读取块长度-->读取块长度的数据-->写入文件-->直到累计接收的数据量等于文件大小)
1.server.py:创建socket,绑定,监听-->接受客户端连接-->接收文件信息-->创建目标文件-->循环接收数据块-->关闭连接和文件
                            (读取文件名长度-->根据长度读取文件名-->读取文件大小)

2.连接服务器-->发送文件信息-->分块读取文件-->每个块前发送字节长度,再发送数据-->文件发送完毕关闭连接
     (发送文件名长度-->发送文件名-->发送文件大小)

项目开发流程
需求分析 -->设计阶段 -->实现阶段 -->测试阶段 -->试验阶段 -->维护阶段

线程学习案例

import time
import threading

lock_object = threading.Lock()

shared_counter = 0

def task(name):
    global shared_counter

    with lock_object:

        print(f"线程:{name}开始工作！")

        for _ in range(5):

            time.sleep(1)

            current = shared_counter

            current += 1

            shared_counter = current

            print(f"线程{name}增加计数器到{shared_counter}")

            print(threading.active_count())      #返回正在运行的线程数量

    print(f"线程{name}完成工作！")


if __name__ == "__main__":

    threads = [
        threading.Thread(target=task, args=('Threading_one',)),

        threading.Thread(target=task, args=('Threading_two',)),

        threading.Thread(target=task, args=('Threading_three',))
    ]

    for t in threads:

        t.start()

    for t in threads:

        t.join()

    print(f"{shared_counter}")



订单处理系统案例(多线程 + 多进程)

import time
import queue
import threading
import multiprocessing

lock = threading.Lock()
lock_object = multiprocessing.RLock()

task_queue = multiprocessing.Queue()   # multiprocessing.Queue是一个线程和进程安全的队列实现,用于在多个进程之间传递数据

   #模拟生成订单任务
for i in range(1,5):

    task_queue.put(f"北京地区订单{i}")

for i in range(1,5):

    task_queue.put(f"上海地区订单{i}")

for i in range(1,5):

    task_queue.put(f"江西地区订单{i}")


  #定义工人处理任务函数
def worker(task_queue_region):

    with lock:

        while True:

            task = task_queue_region.get()   #获取任务

            if task is None:

                break

            print(f'正在处理{task}')

            time.sleep(1)

            print(f'处理完成{task}')

        task_queue_region.task_done()     # Queue.task_done()函数向任务已经完成的队列发送一个信号


#定义每个进程处理特定区域的任务
def process_orders(region,tasks,lock_object):

    try:

        with lock_object:

            task_queue_region = queue.Queue()     #特定区域的任务队列

            while True:

                if task_queue_region.qsize() != 4:

                    task = tasks.get()

                    if region in task:

                        task_queue_region.put(task)

                    else:

                         tasks.put(task)

                else:

                    break

    except Exception as e:

        print(f"Error in process_orders for {region}:{e}")


    threads = []

    for _ in range(2):

        thread = threading.Thread(target = worker,args = (task_queue_region,))

        thread.start()

        threads.append(thread)

    task_queue_region.join()


    #向线程发出退出信号
    for _ in threads:

        task_queue_region.put(None)

    for thread in threads:

        thread.join()


if __name__ == "__main__":

     #创建多进程,处理特定区域订单
    regions = ["北京","上海","江西"]

    processes = []

    for region in regions:

        process = multiprocessing.Process(target = process_orders,args = (region,task_queue,lock_object))

        process.start()

        processes.append(process)

    for process in processes:

        process.join()



线程池学习案例

import time
import random
import threading
import concurrent.futures
lock_object = threading.RLock()


def outer(func):

    def inner(*args,**kw):

        start_time = time.time()

        func(*args,**kw)

        end_time = time.time()

        print(f"耗时:{end_time - start_time:.2f}s")

    return inner


@outer
def task(task_id):

    with lock_object:

        thread_name = threading.current_thread().name

        print(f'线程ID:{thread_name}执行任务{task_id}')

        print(f'任务{task_id}完成')

        time.sleep(random.randint(0,5))


def main():

    with concurrent.futures.ThreadPoolExecutor(5) as executor:

        futures = [executor.submit(task,i) for i in range(5)]

        for future in concurrent.futures.as_completed(futures):

            try:

                future.result()

            except Exception as e:

                print(f"任务执行异常: {e}")

if __name__ == "__main__":

    main()

    print(f'所有任务都已经完成！')



进程池学习案例

import time
import random
import multiprocessing
from concurrent.futures import ProcessPoolExecutor


def calculate_square(number,lock):

    with lock:

        start = time.time()

        print(f"进程{multiprocessing.current_process().name}开始计算{number}的平方")

        time.sleep(random.uniform(0.5,2))

        res = number ** 2

        end = time.time()

        print(res)

        print(f"耗时:{end - start: .2f}s")


if __name__ == "__main__":

    pool = ProcessPoolExecutor(3)

    lock_object = multiprocessing.Manager().RLock()

    futures = [pool.submit(calculate_square,number,lock_object) for number in range(3)]

    for future in futures:

        future.result()

    pool.shutdown(True)

    print(f'所有任务都已经完成！')



#学生成绩管理系统(未涉及数据库、GUI编程)
def add_student(array):

    student_dict = {}

    try:
        id = input("请输入学生学号: ")
        for i in range(len(array)):
            if array[i]['id'] == id:
                print("该学号已经存在")
                return
        name = input("请输入学生姓名: ")
        age = input("请输入学生年龄: ")
        chinese = int(input("请输入学生语文成绩: "))
        math = int(input("请输入学生数学成绩: "))
        english = int(input("请输入学生英语成绩: "))
        student_dict['id'] = id
        student_dict['name'] = name
        student_dict['age'] = age
        student_dict['chinese'] = chinese
        student_dict['math'] = math
        student_dict['english'] = english
        student_dict['score'] = english + math + chinese
        array.append(student_dict)
        print("添加成功")

    except BaseException as e:
        print(f"{str(e)}")

def delete_student(array):

    try:
        id = input("请输入要删除的学生学号: ")
        for i in range(len(array)):
            if array[i]['id'] == id:
                del array[i]
                return 0
        return 1

    except BaseException as e:
        print(f'{str(e)}')

def update_student(array):

    try:
        id = input("请输入要修改的学生学号: ")
        for i in range(len(array)):
            if array[i]['id'] == id:
                name = input("请输入要修改的学生姓名: ")
                age = input("请输入要修改的学生年龄: ")
                chinese = int(input("请输入要修改的学生语文成绩: "))
                math = int(input("请输入要修改的学生数学成绩: "))
                english = int(input("请输入要修改的学生英语成绩: "))
                array['id'] = id
                array['name'] = name
                array['age'] = age
                array['chinese'] = chinese
                array['math'] = math
                array['english'] = english
                array['score'] = english + math + chinese
                print("修改成功")
                return
        print("没找到学号,无法修改")

    except BaseException as e:
        print(f'{str(e)}')

def select_student(array):

    try:
        id = input("请输入要查询的学生学号: ")
        for i in range(len(array)):
            if array[i]['id'] == id:
                print("学生信息: ",array[i])
        return

    except BaseException as e:
        print (f'{str(e)}')
        return


print("学生成绩管理系统案例")
print("**" * 30)
print("欢迎使用学生成绩管理系统")

print("1. 添加学生信息")
print("2. 删除学生信息")
print("3. 修改学生信息")
print("4. 查询学生信息")
print("5. 退出系统")

print("**" * 30)


input_num = 0
array = []

while input_num != 1:
    step = int(input("请输入你的操作"))
    break

if step == 1:
    add_student(array)
    print("学生信息: ",array)

if step == 2:
    num = delete_student(array)
    if num == 0:
        print("删除操作成功")
    print("删除操作失败")

if step == 3:
    update_student(array)
    print("更新之后的学生个人信息: ", array)

if step == 4:
    select_student(array)
    print("学生个人信息: ", array)

input_num = 1
print("退出系统成功")
"""
#新版石头剪刀布游戏
import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4

#值是键击败的对象列表
victories = {
    Action.Scissors: [Action.Lizard, Action.Paper],
    Action.Paper: [Action.Spock, Action.Rock],
    Action.Rock: [Action.Lizard, Action.Scissors],
    Action.Lizard: [Action.Spock, Action.Paper],
    Action.Spock: [Action.Scissors, Action.Rock]
}

def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

def determine_winner(user_action, computer_action):
    defeats = victories[user_action]
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif computer_action in defeats:
        print(f"{user_action.name} beats {computer_action.name}! You win!")
    else:
        print(f"{computer_action.name} beats {user_action.name}! You lose.")

while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = get_computer_selection()

    determine_winner(user_action, computer_action)


    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break