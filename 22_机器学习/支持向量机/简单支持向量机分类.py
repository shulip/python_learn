#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import numpy as np
from sklearn.datasets import load_iris,make_moons
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures     # PolynomialFeatures包含多项式特征
from sklearn.svm import LinearSVC, SVC

from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split


# 绘图函数
def plot_svc_decision_function_another(clf, X, y, tt, axarr=None):

    if axarr is None:
        axarr = plt.gca()
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))
    # f, axarr = plt.subplots(2, 2, sharex='col', sharey='row', figsize=(10, 8))
    # idx = (0,1)
    # for idx, clf, tt in zip(product([0, 1], [0, 1]),
    #                         [clf1, clf2, clf3, eclf],
    #                         ['Decision Tree (depth=4)', 'KNN (k=7)',
    #                          'Kernel SVM', 'Soft Voting']):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)



    axarr.contourf(xx, yy, Z, alpha=0.4)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap='GnBu')
    # axarr.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor='k')
    axarr.set_title(tt)
    plt.show()

def plot_svc_decision_function(model, ax=None, plot_support=True):
    """Plot the decision function for a 2D SVC"""
    if ax is None:
        ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # create grid to evaluate model
    x = np.linspace(xlim[0], xlim[1], 30)
    y = np.linspace(ylim[0], ylim[1], 30)
    Y, X = np.meshgrid(y, x)
    xy = np.vstack([X.ravel(), Y.ravel()]).T
    P = model.decision_function(xy).reshape(X.shape)

    # plot decision boundary and margins
    ax.contour(X, Y, P, colors='k',
               levels=[-1, 0, 1], alpha=0.5,
               linestyles=['--', '-', '--'])

    # plot support vectors
    if plot_support:
        ax.scatter(model.support_vectors_[:, 0],
                   model.support_vectors_[:, 1],
                   s=300, linewidth=1, facecolors='none');
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)


def iris_class_linear():
    # 获取数据
    iris = load_iris()

    # 处理数据，找出特征值和目标值
    X = iris["data"][:, (2, 3)]  # petal length,petal width   # 多维数组切片
    # print(X)
    # print(iris)
    y = (iris["target"] == 2).astype(np.float64)
    # print(y)

    # 分割数据
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    # 特征化工程（标准化）
    std = StandardScaler()

    # 对测试集和训练集的特征值进行标准化
    # x_train = std.fit_transform(x_train)
    # x_test = std.transform(x_test)

    # 进行算法流程
    liner_svc = SVC(C=1, kernel='linear')
    # fit,predict,score
    liner_svc.fit(X, y)

    # 得出预测结果
    # y_predict = liner_svc.predict(x_test)

    # print("得出准确率：",liner_svc.score(X,y))
    print(liner_svc.predict([[5.5, 1.7]]))

    # 画图
    # plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap='autumn')
    # plot_svc_decision_function(liner_svc)
    plot_svc_decision_function_another(liner_svc,X,y,'SCV_linear')
    # plt.show()

def moon_class_PolynomialFeatures():
    moons = make_moons()
    print(moons)

def kernel_svm():
    moons = make_moons()

    # 处理数据，找出特征值和目标值
    #print(moons)
    X = moons[0]
    y = moons[1]
    # print(X)
    # print(y)

    # 特征化工程（标准化）
    std = StandardScaler()

    # 进行算法流程
    # clf = SVC(kernel='poly',degree=3,coef0=100,C=5)
    clf = SVC(kernel='rbf',gamma=1, C=5)

    clf.fit(X,y)
    plot_svc_decision_function_another(clf, X, y, 'SCV_poly')
    # plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap='autumn')
    # plot_svc_decision_function(clf)
    # plt.show()

if __name__ == '__main__':
    # iris_class_linear()
    # moon_class_PolynomialFeatures()
    kernel_svm()
