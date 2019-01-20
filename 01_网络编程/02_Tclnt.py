#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from socket import *

def main():
    # 创建tcp套接字
    tcp_socket = socket(AF_INET,SOCK_STREAM)

    # 连接服务器

    HOST = gethostname()
    PORT = 5691
    BUFSIZE = 1024
    ADDR = (HOST,PORT)
    tcp_socket.connect(ADDR)
    # 发送数据/接收数据
    while True:
        send_data = input(">")
        tcp_socket.send(send_data.encode("utf-8"))

        recv_data = tcp_socket.recv(BUFSIZE).decode("utf-8")

        print(recv_data)

    # 关闭套接字
    tcp_socket.close()

if __name__ == '__main__':
    main()