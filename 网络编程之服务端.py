"""
TCP编程(主动发起连接的是客户端，被动连接的是服务器,用于建立可靠连接)
server.py
import socket

def socket_server():

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.bind(('127.0.0.1',8100))              # gethostname() 获取本机名

    s.listen(10)

    while True:     #持续等待客户的请求维持服务端的运转

        conn,address = s.accept()

        conn.sendall('欢迎学习python网络编程'.encode("UTF-8"))

        client_data = conn.recv(1024)

        if not client_data or client_data.decode("UTF-8") == "exit":

            break

        print(f"{client_data.decode('UTF-8')}")

        conn.sendall(f"hello,{client_data.decode('UTF-8')}".encode("UTF-8"))

        conn.close()

    s.close()

def main():

    socket_server()

if __name__ == "__main__":

    main()

UDP编程(不需要建立连接，只需要知道ip地址与端口号.传输数据不可靠，但是优点是速度快,多用于传输不要求可靠到达的数据)
import socket

def socket_server():

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    sock.bind(("127.0.0.1",8100))

    while True:

        data,address = sock.recvfrom(1024)   #recvfrom()接受UDP数据，返回值是(data,address)

        sock.sendto("hello".encode('UTF-8'),address)   #sendto发送UDG数据

    sock.close()

def sock():

    socket_server()

if __name__ == "__main__":

    sock()

三次握手与四次挥手问题
server.py
三次握手:client.py请求与server.py连接 --> server.py同意连接 --> 建立连接
四次挥手:client.py请求关闭连接 --> server.py确认关闭 --> server.py也准备关闭连接 --> 连接正式关闭

import socket
def socket_server():

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    sock.bind(('127.0.0.1',8100))

    sock.listen(5)

    print("Server listening...")

    conn,address = sock.accept()

    print(f"Connected by {address}")

    conn.close()

    sock.close()


#网络编程中的粘包问题(如果发送端连续快速的发送多条消息,接收端在读取的时候会认为这是一条消息,即两条数据的包粘在一起)
import socket
import struct

def socket_server():

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.bind(('127.0.0.1',8100))

    s.listen(5)

    conn,addr = s.accept()

    
    header_1 = conn.recv(4)

    data_len_1 = struct.unpack("i",header_1)[0]

    print(conn.recv(data_len_1).decode('utf-8'))


    header_2 = conn.recv(4)

    data_len_2 = struct.unpack("i", header_2)[0]

    print(conn.recv(data_len_2).decode('utf-8'))


    conn.close()

    s.close()

def main():

    socket_server()

if __name__ == "__main__":

    main()

#非阻塞与IO多路复用(实现让TCP服务端同时处理多个客户端的请求)
import socket
import select

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.setblocking(False)

sock.bind(('127.0.0.1',8100))

sock.listen(5)


inputs = [sock,]

while True:

    r = select.select(inputs,[],[],0.05)

    for server in r:

        if server == sock:

            conn,address = sock.accept()

            inputs.append(conn)

        else:

            data = sock.recv(1024)

            if data:

                print("sock.recv(1024).decode('utf-8')")

            else:

                print('关闭连接')

                inputs.remove(sock)

简单异步TCP服务器回显
from threading import Thread
import socket

def task(conn):

    while True:

        msg = conn.recv(1024)

        conn.sendall(msg)

def func():

    task(conn)

if __name__ == "__main__":

    func()

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind(("127.0.0.1",8100))

sock.listen(5)

while True:

    conn,addr = sock.accept()

    t = Thread(target = task,args = (conn,))

    t.daemon = True

    t.start()
"""