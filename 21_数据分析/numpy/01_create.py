#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import numpy as np

# array(深拷贝)
# asarray(浅拷贝)


'''创建简单数组'''
""" 
# a = [1,2,3,4]
a = [[1],[2],[3],[4]]
b = np.array(a)

print(a)
print(b)
# 查看数组属性
print(b.size)       # 数组元素的个数
print(b.shape)      # 数组形状
print(b.ndim)       # 数组维度
print(b.dtype)      # 数组元素类型
"""


'''快速创建N维数组的api函数'''
"""
array_one = np.ones([10,10])        # 创建10行10列的数值为浮点1的矩阵
array_zeros = np.zeros([10,10])     # 创建10行10列的数值为浮点0的矩阵
print(array_one)
print(array_zeros)
"""


'''创建随机数组'''

"""
# 均匀分布
c = np.random.rand(10,10)           # 创建指定形状(示例为10行10列)的数组(范围在0至1之间)
d = np.random.uniform(0,100)        # 创建指定范围内的一个数
e = np.random.randint(0,100)        # 创建指定范围内的一个整数
print(c)
print('*'*30)
print(d)
print('*'*30)
print(e)
"""

# 正态分布
arr = np.random.normal(1.75,0.1,(4,5))      # 给定均值/标准差/维度的正态分布
print(arr)

after_arr = arr[1:3,2:4]
print(after_arr)

# 改变数组的形状
# (要求前后元素个数匹配)
print('reshape函数的使用')
one_20 = np.ones([20])
print("-->1行20列<--")
print(one_20)

one_4_5 = one_20.reshape([4,5])
print("-->4行5列<--")
print(one_4_5)


