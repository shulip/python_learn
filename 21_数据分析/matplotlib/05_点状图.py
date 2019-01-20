#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from matplotlib.font_manager import *
from matplotlib import pyplot as plt
import numpy as np

myfont = FontProperties(fname='F:\编程工程\python\matplotlib/msyh.ttc',size = 40)


plt.figure(figsize=(20,16),dpi=100,linewidth=20)

_x_move = np.array([3,2,1])
_y_move = np.array([104,100,81])

_x_love = np.array([101,99,98])
_y_love = np.array([10,5,2])

_x_unknow = np.array([18])
_y_unknow = np.array([90])

move = plt.plot(_x_move,_y_move,'ro',label="动作片",color="#823384")
plt.setp(move, markersize=30)

love = plt.plot(_x_love,_y_love,'ro',label="爱情片",color="b")
plt.setp(love, markersize=30)

unknow = plt.plot(_x_unknow,_y_unknow,'ro',label="未知",color="r")
plt.setp(unknow, markersize=30)

# 生成打斗镜头的描述
x_ = [x_ for x_ in range(0,120)][::20]
# 设置x轴显示
plt.xticks(x_,x_,fontproperties=myfont,size = 40)

# 生成接吻镜头的描述
y_ = [y_ for y_ in range(0,120)][::20]
# 设置y轴显示
plt.yticks(y_,y_,fontproperties=myfont,size = 40)

# 设置x,y轴名称
plt.xlabel("次数",fontproperties=myfont,size = 50)
plt.ylabel("次数",fontproperties=myfont,size = 50)

# 显示网络
plt.grid(True,linestyle="--",alpha=0.5,linewidth=3)

# 显示图例
plt.legend(loc="best",prop=myfont,fontsize = 300)

# 指定标题
plt.title("电影分类",fontproperties=myfont,size = 70)

plt.savefig('1.png')
plt.show()
