#!/usr/bin/env python 
# -*- coding:utf-8 -*-

"""
任何实现了__enter__()和__exit__()方法的对象都可称为上下文管理器
产生异常必调用关闭，释放资源
文件，数据库连接，套接字
"""

class File():
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.f = open(self.filename,self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()

with File("out.txt",'w') as f:
    f.write("Hello world!!")

"""*******************另类套接字*********************"""

