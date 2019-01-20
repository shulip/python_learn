#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from matplotlib import pyplot as plt
from matplotlib.font_manager import *
import random

# 字体
myfont = FontProperties(fname='F:\编程工程\python\matplotlib/msyh.ttc')

# 学习时间分配
pro_name = ["C++", "Python", "Java", "Go", "Swift"]
pro_time = [10, 15, 5, 3, 1]

# 画饼
plt.pie(pro_time,labels=pro_name,autopct="%3.2f%%", colors=["#ea6f5a", "#509839", "#0c8ac5", "#d29922", "#fdf6e3"])

# 指定标题
plt.title("学习时间分配",fontproperties=myfont)

# 保证图像为正圆
plt.axis("equal")

# 显示图像
plt.legend(loc="best")
plt.show()