#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pandas as pd
from sklearn.decomposition import PCA


# 读取四张表的数据
print('1')
prior = pd.read_csv('data\\order_products__prior.csv')
print('1')
products = pd.read_csv('data\\products.csv')
print('1')
orders = pd.read_csv("data\\orders.csv")
print('1')
aisles = pd.read_csv("data\\aisles.csv")
print('2')
# 合并四张表到一张表     （用户-物品类别）
_mg = pd.merge(prior,products,on=['product_id','product_id'])
print('3')
_mg = pd.merge(_mg,orders,on = ['order_id','order_id'])
print('4')
mt = pd.merge(_mg,aisles,on = ['aisle_id','aisle_id'])
print('5')

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

print(mt.head(10))

# 交叉表（特殊的的分组工具）
cross = pd.crosstab(mt['user_id'],mt['aisle'])

# 进行主成分分析
pca = PCA(n_components=0.9)

data = pca.fit_transform(cross)