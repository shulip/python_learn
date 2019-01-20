#!/usr/bin/env python 
# -*- coding:utf-8 -*-

"""物以类聚，人以群分"""
# 聚类一般做在分类之前
"""api:sklearn.cluster.KMeans"""



import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt


# 读取四张表的数据
prior = pd.read_csv('data\\order_products__prior.csv')
products = pd.read_csv('data\\products.csv')
orders = pd.read_csv("data\\orders.csv")
aisles = pd.read_csv("data\\aisles.csv")
# 合并四张表到一张表     （用户-物品类别）
_mg = pd.merge(prior,products,on=['product_id','product_id'])
_mg = pd.merge(_mg,orders,on = ['order_id','order_id'])
mt = pd.merge(_mg,aisles,on = ['aisle_id','aisle_id'])

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

print(mt.head(10))

# 交叉表（特殊的的分组工具）
cross = pd.crosstab(mt['user_id'],mt['aisle'])

# 进行主成分分析
pca = PCA(n_components=0.9)

data = pca.fit_transform(cross)

# 把样本数量减少
x = data[:500]

# 假设用户有四个类别
km = KMeans(n_clusters=4)
km.fit(x)

predict = km.predict(x)

print(predict)

