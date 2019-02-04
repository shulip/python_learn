#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# pythonic
file = "test.txt"
with open(file) as f:
    data = f.read()

print(data)
print("*"*20)

# 普通写法
f = open(file)
try:
    data_1 = f.read()
finally:
    f.close()

print(data_1)