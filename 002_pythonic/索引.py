#!/usr/bin/env python 
# -*- coding:utf-8 -*-

num_list = [1,4,9]
# pythonic
for i,val in enumerate(num_list):
    print(i,"--->",val)

print("*"*20)

# 普通写法
for i in range(len(num_list)):
    print(i,"--->",num_list[i])

