#!/usr/bin/env python 
# -*- coding:utf-8 -*-

"""
GIL：全局解释锁
多线程：适合I/O密集型程序，不适合计算密集型程序
多进程：计算密集型

计算密集型程序：进程
I/O密集型程序：线程，协程
"""

from threading import Thread
from multiprocessing import process


def fun1():
    """
    单线程死循环
    一个线程占了一个cpu核
    """
    while True:
        pass


def fun2():
    """
    多线程死循环

    """
    t1 = Thread(target=fun1)
    t1.start()


if __name__ == '__main__':
    fun2()
