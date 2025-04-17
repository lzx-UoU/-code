"""
TCP编程
import socket

def socket_client():

    client = socket.socket()

    client.connect(("127.0.0.1",8100))

    print(f"{client.recv(1024).decode('UTF-8')}")

    client.sendall("python".encode('utf-8))

    print(client.recv(1024).decode("UTF-8"))

    client.close()

def main():

    socket_client()

if __name__ == "__main__":

    main()

UDP编程
import socket

def socket_client():

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    for data in [b"python",b"java"]:

        s.sendto(data,("127.0.0.1",8100))

        print(s.recv(1024).decode('UTF-8'))

    s.close()

def main():

    socket_client()

if __name__ == "__main":

    main()

三次握手与四次挥手问题
client.py

import socket
def socket_client():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(('127.0.0.1',8100))

    client.close()

#网络编程中的粘包问题
import socket
import struct
def socket_client():

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #client.setblocking(False)   #使阻塞变为非阻塞

    client.connect(('127.0.0.1',8100))


    data_1 = "learn".encode('utf-8')

    header_1 = struct.pack("i",len(data_1))

    client.sendall(header_1)

    client.sendall(data_1)


    data_2 = "python".encode('utf-8')

    header_2 = struct.pack("i",len(data_2))

    client.sendall(header_2)

    client.sendall(data_2)


    client.close()

def main():

    socket_client()

if __name__ == "__main__":

    main()

#非阻塞与IO多路复用(实现让TCP服务端同时处理多个客户端的请求)
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1',8100))

while True:

    content = input("xxx")

    if 'content.upper()' == b"None":

        break

    client.sendall(content.encode('utf-8'))

client.close()
"""







