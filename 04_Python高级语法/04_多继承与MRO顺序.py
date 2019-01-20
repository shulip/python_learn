#!/usr/bin/env python 
# -*- coding:utf-8 -*-

class Parent(object):
    def __init__(self, name):
        print("父类开始")
        self.name = name
        print("父类结束")


class Son1(Parent):
    def __init__(self, name):
        print("子1开始")
        self.name = name
        super().__init__(name)
        # Parent.__init__(self, name)
        print("子1结束")


class Son2(Parent):
    def __init__(self, name):
        print("子2开始")
        self.name = name
        super().__init__(name)
        # Parent.__init__(self, name)
        print("子2结束")


class Grandson(Son1, Son2):
    def __init__(self, name, age):
        # son1.__init__(self,name)
        super().__init__(name)# 等价于 super(Grandson，self).__init__(name)
        # super(Son1，self).__init__(name) 从Son1向mro搜索

        self.age = age


if __name__ == '__main__':
    a = Grandson('aa', 23)
    print(Grandson.__mro__) # 使用C3算法
    # (<class '__main__.Grandson'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class '__main__.Parent'>, <class 'object'>)
    print(a.name, a.age)
