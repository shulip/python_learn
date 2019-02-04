#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# pythonic
odd = [i for i in range(1,100) if i%2==1]

a_set = [i for i in range(1,200)]
b_set = [i for i in range(89,123)]
result = [(x,y) for x in a_set for y in b_set if x+y>100]

# 普通写法
result_1 = []
for i in range(100):
    if i%2 ==1:
        result.append(i)

result_2 = []
for x in a_set:
    for y in b_set:
        if x+y>100:
            result_2.append((x,y))

