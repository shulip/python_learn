#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm "+self.name+' @ '+str(i) # name属性中保存的是当前线程的名字
            print(msg)

    def login(self):
        print("这是登录")

    def register(self):
        print("这是注册")

if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread()
    t1.start()
    t2.start()