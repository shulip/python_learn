#!/usr/bin/env python 
# -*- coding:utf-8 -*-


"""
__new__：创建对象，开辟内存空间
__init__:对空间进行初始化

"""
# 类对象
class Province(object):
    # 类属性
    country = "中国"

    def __init__(self,name):
        # 实例属性
        self.name = name

    # 实例方法
    def ord_fun(self):
        """定义实例方法，至少有一个self参数"""
        print("实例方法")

    # 静态方法，和类对象和实例对象都无关
    @staticmethod
    def static_fun():
        """定义静态方法，无默认参数"""
        print("静态方法")

    # 类方法
    @classmethod
    def class_fun(cls):
        """定义类方法，至少有一个cls参数"""
        cls.country = '还是中国ang'



# 实例对象
obj = Province("江苏")
print(obj.country)
print(Province.country)

print('---------------')
obj.country = "还是中国"
print(obj.country)
print(Province.country)

print('---------------')
obj.__class__.country = "还是中国"
print(obj.country)
print(Province.country)

print('---------------')
obj.class_fun()
print(obj.country)
print(Province.country)
print(obj.name)

