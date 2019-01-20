#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import numpy as np

a = np.arange(24).reshape(4,6)
print(a)
print(type(a[0,0]))
# 替换类型
# a.astype()

# 小于10的变为0，否则变为1
b = np.where(a<10,0,1)
print(b)

# 小于10的替换为10，大于18的替换为18
c = a.clip(10,18)
print(c)

a[a<10] = 98
print(a)