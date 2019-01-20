#!/usr/bin/env python 
# -*- coding:utf-8 -*-


"""简洁！！！"""

class Foo(object):
    def fun(self):
        print("1")

    # 定义property属性
    @property
    def prop(self):
        print('2')

    @property
    def size(self):
        return 100


"""*************调用*************"""
# foo_obj = Foo()
# foo_obj.fun()
# foo_obj.prop
# ret = foo_obj.size

"""****************************************"""
class Pager(object):
    def __init__(self, current_page):
        # 用户当前请求的页码
        self.current_page = current_page

        # 默认每页显示10条数据
        self.per_items = 10

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items
        return val



# p = Pager()
# print(p.start)  # 起始值，即：m
# print(p.end)  # 结束值，即：n

"""****************************************"""
class Goods(object):
    """python3中默认继承object"""
    def __init__(self):
        self.ori_price = 100
        self.count = 0.8
    """第一种方式,取值"""
    @property
    def price(self):
        # print("@property")
        new_price = self.ori_price * self.count
        return new_price
    """第二种方式，设置值"""
    @price.setter
    def price(self,value):
        # print('@price.setter')
        self.ori_price = value
    """第三种方式，删除值"""
    @price.deleter
    def price(self):
        # print('@price.deleter')
        del self.ori_price


# obj = Goods()
# print(obj.price)
# obj.price = 200
# del obj.price
"""****************************************"""

class Fooo(object):

    def __init__(self):
        self.bar = 20
    def get_bar(self):
        return self.bar

    def set_bar(self,value):
        self.bar = value

    def del_bar(self):
        del self.bar
    # property
    # def __init__(self, fget=None, fset=None, fdel=None, doc=None)
    BAR = property(get_bar,set_bar,del_bar)
"""****************************************"""

# 使用property升级getter和setter方法
class Money(object):
    def __init__(self):
        self.__money = 100

    def get_money(self):
        return self.__money

    def set_money(self,value):
        if isinstance(value,int):
            self.__money = value
        else:
            print("error:输入类型错误")

    money = property(get_money,set_money)

m = Money()

print(m.money)
m.money = 200
print(m.money)