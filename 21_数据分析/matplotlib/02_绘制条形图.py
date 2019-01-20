#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from matplotlib import pyplot as plt
from matplotlib.font_manager import *
import numpy as np
import random

# 字体
myfont = FontProperties(fname='F:\编程工程\python\matplotlib/msyh.ttc')

# 条形图绘制名侦探柯南主要角色的年龄
role_list = ["柯南", "毛利兰", "灰原哀", "琴酒","贝尔摩 特加", "赤井秀一", "目暮十三"]
role_age = [7, 17, 7, 34, 32, 30, 27, 46]

#实际年龄
role_ture_age = [18, 17, 18, 34, 45, 30, 27, 46]

x = np.array([i for i in range(1,len(role_list)+1)])

y = role_age
y2 = role_ture_age

# 设置画板属性
plt.figure(figsize=(15,8),dpi=200)

# width以x为基准，向右为正，向左为负(如果多了,就需要为基准x加减响应的数值)
plt.bar(x,y,width=0.3,label='现实年龄',color="#509839")
plt.bar(x+0.3,y2,width=0.3,label='实际年龄',color="#c03035")

x_ = [i for i in range(1,len(role_list)+1)]
x_desc = ["{}".format(x_desc) for x_desc in role_list]
x_desc.insert(0,"")

y_ = range(50)[::5]
y_desc = ["{}岁".format(y_desc) for y_desc in y_]

# 设置x,y轴的数值和特征描述
plt.xticks(x_,x_desc,fontproperties=myfont)
plt.yticks(y_,y_desc,fontproperties=myfont)

plt.xlabel("角色名称",fontproperties=myfont)
plt.ylabel("年龄",fontproperties=myfont)
plt.title("名侦探柯南主要角色年龄(部分)")

plt.legend(loc="best",prop=myfont)
plt.show()