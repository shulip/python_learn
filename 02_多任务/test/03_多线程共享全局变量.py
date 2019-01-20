#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import threading
import time

num = 100
nums = [11,22]


def test1():
    global num
    num += 100


def test2():
    nums.append(33)

print(num)
print(nums)
test1()
test2()
print(num)
print(nums)