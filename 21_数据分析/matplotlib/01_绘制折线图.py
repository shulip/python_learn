#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from matplotlib.font_manager import *
from matplotlib import pyplot as plt
import random

# 保证生成的图片在浏览器内显示
# %matplotlib inline
# 保证能正常显示中文(Mac)
# plt.rcParams['font.family'] = ['Arial Unicode MS']
myfont = FontProperties(fname='F:\编程工程\python\matplotlib/msyh.ttc')
# plt.rcParams['font.family'] = ['msyh.ttc']
# 模拟海南一天的温度变化

# 生成x轴的24小时
hainan_x = [h for h in range(0,24)]

# 生成y轴的温度随机值（15,25）
hainan_y = [random.randint(15,25) for t in range(0,24)]

# 设置画板属性
plt.figure(figsize=(100,80),dpi=100)

# 往画板绘图
plt.plot(hainan_x,hainan_y,label="海南")

# 模拟北京一天的温度变化

# 生成x轴的24小时
beijing_x = [h for h in range(0,24)]

# 生成y轴的温度随机值（15,25）
beijing_y = [random.randint(5,10) for t in range(0,24)]

# 往画板绘图
plt.plot(beijing_x,beijing_y,label="北京")

# 模拟北京一天的温度变化
hebei_x = beijing_x
hebei_y = [random.randint(1, 5) for t in range(0, 24)]

# 自定义绘制属性: 颜色color="#0c8ac5", linestyle"-"""--""-.":", 线宽linewidth, 透明度alpha
plt.plot(hebei_x,hebei_y,label="河北",color="#823384",linestyle=":",linewidth=3,alpha=0.3)

# 生成24小时的描述
x_ = [x_ for x_ in range(0,24)]
x_desc = ["{}时".format(x_desc) for x_desc in x_]

# 设置x轴显示24小时
plt.xticks(x_,x_desc,fontproperties=myfont)

# 生成10至30度的描述
y_ = [y_ for y_ in range(0, 30)][::2]
y_desc = ["{}℃".format(y_desc) for y_desc in y_]

# 设置y轴显示温度描述
plt.yticks(y_, y_desc,fontproperties=myfont)

# 设置x,y轴名称
plt.xlabel("时间",fontproperties=myfont)
plt.ylabel("温度",fontproperties=myfont)

# 指定标题
plt.title("一天内温度的变化",fontproperties=myfont)

# 显示图例
plt.legend(loc="best",prop=myfont)

plt.show()
