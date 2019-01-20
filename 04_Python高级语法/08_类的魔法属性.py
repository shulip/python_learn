#!/usr/bin/env python 
# -*- coding:utf-8 -*-

"""
__doc__:类的描述信息
__class__:显示所属类
__module__:显示所属模块
__new__:开辟空间
__init__:初始化
__del__：析构函数
__call__:对象后面加小括号()自动调用
__dict__:检查类或实例对象所有属性
__str__:当定义__str__，在为得到对象描述时，默认输出该函数返回值（int,str,bool都可以）
__getitem__/__setitem__/__delitem__:用于索引操作，如字典,对象加中括号[]。获取/设置/删除数据
__getslice__/__setslice__/__delslice__:用于切片操作，如列表
____:
"""

class Dog(object):
    """这是狗狗哦"""
    def __init__(self,name):
        self.name = name


d = Dog("hsq")

print(d.__doc__)