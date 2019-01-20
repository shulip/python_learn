#!/usr/bin/env python 
# -*- coding:utf-8 -*-

"""
api:class sklearn.tree.DecisionTreeClaasifier(criterion='gini',max_depth=None,random_state=None)
- 决策树分类器
- criterion：默认是‘gini’系数，也可以选择信息增益的熵'entropy'
- max_depth：树的深度大小
- random_state:随机数种子

- method:
- decision_path:返回决策树的路径
"""

import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV


def decision():
    """
    决策树对泰坦尼克号进行预测生死
    :return: None
    """
    # 获取数据
    titan = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")

    # 处理数据，找出特征值目标值
    x = titan[['pclass','age','sex']]

    y = titan['survived']

    print(x)
    # 缺失值处理
    x['age'].fillna(x['age'].mean(),inplace=True)

    # 分割数据
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)


    # 进行处理（特征过程）特征->类别->one_hot编码
    dict = DictVectorizer(sparse=False)

    x_train = dict.fit_transform(x_train.to_dict(orient="records")) # pd转换字典，特征抽取 # orient="records"表示一行一行改变

    print(dict.get_feature_names())

    x_test = dict.transform(x_test.to_dict(orient="records"))

    # print(x_train)
    dec = DecisionTreeClassifier(max_depth=5)

    dec.fit(x_train,y_train)

    #预测准确率

    param = {'max_depth':[1,2,3,4],'criterion':['gini','entropy']}

    gc = GridSearchCV(dec, param_grid=param, cv=2)

    gc.fit(x_train, y_train)
    print("在测试集上准确率：", gc.score(x_test, y_test))

    print("在交叉验证中验证的最好结果:", gc.best_score_)

    print("最好的参数模型:", gc.best_estimator_)

    print("每次交叉验证后的验证集准确率结果和训练集样本准确率结果", gc.cv_results_)
    # print("预测的准确率：",dec.score(x_test,y_test))

    return None


if __name__ == '__main__':
    decision()


