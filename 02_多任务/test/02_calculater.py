#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import numpy as np

# conditional judgment(条件判断)
stus_score = np.array([[80,88],[82,81],[84,75],[86,83],[75,81]])
print(stus_score > 80)

# 统计运算
# 指定轴最大值amax(参数1: 数组; 参数2: axis=0/1; 0表示列1表示行)
print("每一列的最大值为：")
result_0 = np.amax(stus_score,axis=0)
print(result_0)

print("每一行的最大值为：")
result_1 = np.amax(stus_score,axis=1)
print(result_1)

# 指定轴最小值amin
print("每一列的最小值为：")
result_2 = np.amin(stus_score,axis=0)
print(result_2)

print("每一行的最小值为：")
result_3 = np.amin(stus_score,axis=1)
print(result_3)

# 方差std
print("每一列的方差：")
result_4 = np.std(stus_score,axis=0)
print(result_4)

print("每一行的方差：")
result_5 = np.std(stus_score,axis=1)
print(result_5)



