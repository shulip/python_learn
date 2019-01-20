#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from socket import *
from multiprocessing import Process
import threading

BUFSIZE = 1024


def send_msg(udp_socket):
    """
    发送消息
    :param udf_socket: 套接字
    :return:None
    """
    send_data = input("请输入发送的消息:")
    dest_ip = input("请输入对方的ip：")
    dest_port = input("请输入对方的端口：")
    udp_socket.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """
    接收数据
    :param udp_socket:套接字
    :return: None
    """
    recv_data, addr = udp_socket.recvfrom(BUFSIZE)

    print("%s:%s" % (str(addr), recv_data.decode("utf-8")))


def main():
    # 创建udp套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    # 绑定信息
    udp_socket.bind("", 7788)
    # 循环处理
    while True:
        # 发送
        send_msg(udp_socket)
        # 接受并显示
        recv_msg(udp_socket)

class user:
    def __init__(self):
        self.BUFSIZE = 1024
        self.PORT = 5691
        self.HOST = gethostname()
        self.AADDR = (self.HOST,self.PORT)
        self.udp_socket = socket(AF_INET,SOCK_DGRAM)

    def send_msg(self):
        """
        发送消息
        :param udf_socket: 套接字
        :return:None
        """
        while True:
            try:
                send_data = input("请输入发送的消息:")
                # dest_ip = input("请输入对方的ip：")
                # dest_port = input("请输入对方的端口：")
                self.udp_socket.sendto(send_data.encode('utf-8'), self.AADDR)
            except EOFError:
                pass


    def recv_msg(self):
        """
            接收数据
            :param udp_socket:套接字
            :return: None
            """
        while True:
            try:
                recv_data, addr = self.udp_socket.recvfrom(BUFSIZE)
                print("%s:%s" % (str(addr), recv_data.decode("utf-8")))
            except OSError:
                pass

    def run(self):
        t1 = Process(target=self.send_msg)
        t2 = Process(target=self.recv_msg)
        t1.start()
        t2.start()

if __name__ == '__main__':
    u = user()
    u.run()
