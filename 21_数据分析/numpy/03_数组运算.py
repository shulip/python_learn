#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import numpy as np

stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])

"""数组与数的运算"""
# 加法
print("加分前：")
print(stus_score)

print("加分后：")
stus_score[:,0] += 5
print(stus_score)

# 乘法
print("减半前：")
print(stus_score)

print("减半后：")
stus_score[:,0] = stus_score[:,0]*0.5
print(stus_score)


"""数组间的运算（基本用不到）"""
a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a+b
d = a-b
e = a*b
f = a/b
print("a+b为",c)
print("a-b为",d)
print("a*b为",e)
print("a/b为",f)
