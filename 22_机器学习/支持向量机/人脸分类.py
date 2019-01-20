#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from __future__ import print_function

from time import time
import logging
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import fetch_lfw_people
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler


def face_clf():
    lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

    # 获取样本数量，高度，宽度
    # print(lfw_people.images.shape)
    n_samples,h,w = lfw_people.images.shape

    # 处理数据，找出特征值和目标值
    X = lfw_people.data
    y = lfw_people.target
    # print(X)

    # 分割数据
    x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.25)

    # 获取特征数目
    # print(X.shape)
    n_features = X.shape[1]

    # 特征化工程（标准化）
    std = StandardScaler()

    # 对测试集和训练集的特征值进行标准化
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    # 数据降维
    pca = PCA(n_components=0.9)
    x_train = pca.fit_transform(x_train)
    x_test = pca.transform(x_test)

    # 进行算法流程
    # param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
    #               'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
    param_grid = {'C': [1000,100,150,130,90],
                  'gamma': [0.0001,0.00005,0.00007,0.00003], }

    # clf = SVC(kernel='rbf', class_weight='balanced',C=100,gamma=0.0001)
    clf = SVC(kernel='rbf', class_weight='balanced')
    gc = GridSearchCV(clf, param_grid=param_grid, cv=5)
    # clf.fit(x_train,y_train)
    gc.fit(x_train, y_train)


    # print("得出准确率：", clf.score(x_test, y_test))
    print("在测试集上的准确率：",gc.score(x_test,y_test))
    print("最好的参数模型:", gc.best_estimator_)




if __name__ == '__main__':
    face_clf()


