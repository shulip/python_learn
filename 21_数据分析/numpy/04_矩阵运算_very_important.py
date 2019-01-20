#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import numpy as np

"""矩阵运算np.dot()(非常重要)"""
"""与@等价"""
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 平时成绩占40%，期末成绩占60%
q = np.array([[0.4],[0.6]])
result = np.dot(stus_score,q)
result_3 = stus_score @ q
print("所有人分数：")
print(stus_score)
print("最终结果：")
print(result)
print(result_3)


"""矩阵拼接"""
print("v1:")
v1 = np.array([[0, 1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10, 11]])
print(v1)
print("v2:")
v2 = np.array([[12, 13, 14, 15, 16, 17],
               [18, 19, 20, 21, 22, 23]])
print(v2)

# 垂直拼接
result_1 = np.vstack((v1,v2))
print("v1和v2垂直拼接的结果为")
print(result_1)

# 水平拼接
result_2 = np.hstack((v1,v2))
print("v1和v2水平拼接的结果为")
print(result_2)