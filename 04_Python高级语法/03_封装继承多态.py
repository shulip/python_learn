#!/usr/bin/env python 
# -*- coding:utf-8 -*-

"""gcc hello_world.cpp -shared -o libhello_world.so"""
class a(object):
    def __init__(self):
        self.__b = 1    # 私有

    def hello(self):
        print(self.__b)

aa = a()

print(aa.__dict__)
print(aa.__class__)