#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from sklearn.datasets import load_iris,fetch_20newsgroups,load_boston

from sklearn.model_selection import train_test_split

li = load_iris()

# print("获取特征值")
# print(li.data)
# print("获取目标值")
# print(li.target)
# print(li.DESCR)

# 返回值：train（训练集） x_train(特征值) y_train（目标值），
#         test(测试集)    x_test(特征值)  y_test（目标值）
# x_train, x_test, y_train, y_test = train_test_split(li.data, li.target, test_size=0.25)
#
# print("训练集特征值和目标值：",x_train,y_train)
# print("测试集特征值和目标值：",x_test,y_test)

# news = fetch_20newsgroups(subset='all')
# print(news.data)
# print(news.target)

lb = load_boston()
print("获取特征值")
print(lb.data)
print("获取目标值")
print(lb.target)
print(lb.DESCR)