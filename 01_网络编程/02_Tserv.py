#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from socket import *
from time import ctime

def main():
    # 创建socket
    tcp_socket = socket(AF_INET,SOCK_STREAM)

    # 本地信息
    HOST = gethostname()
    PORT = 5691
    ADDR = (HOST,PORT)
    BUFSIZE = 1024

    # 绑定
    tcp_socket.bind(ADDR)

    # 监听(被动)
    tcp_socket.listen(128)

    while True:
        # 等待客户端连接
        print("Waiting for connection...")
        tcpCliSock,addr = tcp_socket.accept()
        print("...connect from %s" % str(addr))

        while True:
            # 接收数据
            recv_data = tcpCliSock.recv(BUFSIZE).decode("utf-8")

            if not recv_data:
                break
            # 发送数据
            tcpCliSock.send(("[%s] %s" % (ctime(),recv_data)).encode("utf-8"))

            tcpCliSock.close()
            print("服务器服务完毕")


    tcp_socket.close()

if __name__ == '__main__':
    main()