#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 超参数搜索-网络搜索api
# sklearn.model_selection.GridSearchCV
from sklearn.model_selection import GridSearchCV
"""
sklearn.model_selection.GridSearchCV(estimator,param_grid=None,cv=None)
- 对估计器的指定参数值进行详尽搜索

- estimator:估计器对象
- param_grid:估计器参数（dict）{"n_neighbors":[1,3,5]}
- cv:指定几折交叉验证

- fit:输入训练数据
- score:准确率
- 结果分析:
- best_score:在交叉验证中验证的最好结果
- best_estimator_:最好的参数模型
- cv_results_:每次交叉验证后的验证集准确率结果和训练集样本准确率结果
"""


from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# 读取数据
data = pd.read_csv('data\\FBlocation\\train.csv')

# print(data.head(10))

# 处理数据
# 1、缩小数据,查询数据筛选
data = data.query("x > 1.0 & x < 1.25 & y > 2.5 & y < 2.75")

# 2、处理时间数据
# pd.to_datatime把时间戳转换成时间年月日的形式
# pd.DatetimeIndex 把日期数据转换为字典格式
time_value = pd.to_datetime(data['time'], unit='s')

# print(time_value)
# 把日期格式转换为字典格式
time_value = pd.DatetimeIndex(time_value)

# 构造一些特征
data['day'] = time_value.day
data['hour'] = time_value.hour
data['weekday'] = time_value.weekday

# 把时间戳特征删除
data.drop(['time'], axis=1)  # 这里1表示列，sklearn里面0表示列
# print(data)

# 把签到数量少于n个的目标位置删除
place_count = data.groupby('place_id').count()
# print(place_count)
tf = place_count[place_count.row_id > 3].reset_index()  # 索引从0开始

data = data[data['place_id'].isin(tf.place_id)]

# 取出数据当中的特征值与目标值
y = data['place_id']  # 目标值

x = data.drop(['place_id', 'row_id'], axis=1)  # 特征值

# 进行数据的分割训练集合测试集
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

knn = KNeighborsClassifier()

param = {"n_neighbors":[3,5,10]}

# 进行网络搜索
gc = GridSearchCV(knn,param_grid=param,cv=2)

gc.fit(x_train,y_train)

# 预测准确率
print("在测试集上准确率：",gc.score(x_test,y_test))

print("在交叉验证中验证的最好结果:",gc.best_score_)

print("最好的参数模型:",gc.best_estimator_)

print("每次交叉验证后的验证集准确率结果和训练集样本准确率结果",gc.cv_results_)