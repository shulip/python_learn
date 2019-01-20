#!/usr/bin/env python 
# -*- coding:utf-8 -*-



"""
单工：只能收或只能发（收音机）
半双工：可以双向，但同一时刻只能单向（对讲机）
全双工：可以同时双向（手机）
socket套接字是全双工
"""

from socket import *


def main():
    """"""
    # 1、创建一个udp套接字
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    # 绑定端口
    HOST = gethostname()
    local_addr = ('',5691)
    # 2、准备接收方的ip与端口
    udp_socket.bind(local_addr)
    PORT = 5691
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    try:
        while True:
            # 从键盘获取数据
            send_data = input(">>")

            # 如果输入数据为‘q’就退出
            if send_data=='q':
                break

            # 可以使用套接字收发数据
            # udp_socket.sendto(("示例文字").encode(),())
            udp_socket.sendto((send_data).encode("utf-8"),ADDR)

            # 接受回送过来的数据
            recv_data = udp_socket.recvfrom(BUFSIZ)
            # 套接字可以同时 收发数据
        # 关闭套接字
        udp_socket.close()
    except OSError:
        print("该请求的地址无效")


if __name__ == '__main__':
    main()


