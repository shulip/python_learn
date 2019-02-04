#!/usr/bin/env python 
# -*- coding:utf-8 -*-

"""列表类似顺序表，前插耗大量时间，效率低下"""
from collections import deque

# pythonic
names = deque(['c','d','e'])

print(names)

names.popleft()
names.appendleft('b')
names.append('f')

print(names)

# 普通写法
names_1=list['c','d','e']
names_1.pop()
names_1.insert(0,'b')
names_1.append('f')