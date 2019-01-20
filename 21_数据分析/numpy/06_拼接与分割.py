#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import numpy as np

"""
拼接：
np.vstack((a1,a2,a3...))    竖直拼接(verticallly)
np.hstack((a1,a2,a3...))    水平拼接(horizontally)

分割：
分割与拼接正好相反
"""

a1 = np.arange(12).reshape(2,6)
a2 = np.arange(13,25).reshape(2,6)
print(a1)
print(a2)

a3 = np.vstack((a1,a2))
a4 = np.hstack((a1,a2))
print(a3)
print(a4)