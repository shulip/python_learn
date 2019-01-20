#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from socket import *

def main():
    # 1、创建套接字
    udp_ser_socket = socket(AF_INET,SOCK_DGRAM)

    # 2、绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
    HOST = gethostname()
    PORT = 5691  # 端口
    BUFSIZ = 1024  # 接受的最大字节数
    ADDR = (HOST, PORT)
    udp_ser_socket.bind(ADDR)

    while True:
        # 3、接收数据
        print("等待接收数据")
        recv_data,addr = udp_ser_socket.recvfrom(BUFSIZ)
        # 4、打印接受到的数据
        print("%s:%s" % (str(addr),recv_data.decode("utf-8")))  # jbk,utf-8
    # 5、关闭套接字
    udp_ser_socket.close()
if __name__ == '__main__':
    main()