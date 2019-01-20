#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 1.特征选择
"""
原因：
    冗余
    噪声
主要方法：
    Filter(过滤式):VarianceThreshold(sklearn.feature_selection)
        variance(方差)
    Embedded(嵌入式):正则化，决策树
    神经网络
"""
# 2.主成分分析
"""
sklearn.de
本质：
PCA：简化数据集，特征数量达到上百的时候，考虑数据的简化问题
数据会改变，特征数量也会减少
高维数据，特征数量多，特征容易相关
PCA(n_components = 小数[保留的比例;范围0-1;90%-95%效果比较好]/整数[减少到的特征数量])
"""



from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA


# 1.特征选择
def var():
    """
    特征选择-删除低方差特征
    :return: None
    """
    # var = VarianceThreshold(threshold=1.0)        # 0-10根据实际效果
    var = VarianceThreshold()

    data = var.fit_transform([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])

    print(data)

    return None


def pca():
    """
    主成分分析数据降维
    :return: None
    """
    pca = PCA(n_components=0.9)
    data = pca.fit_transform([[2,8,4,5],[6,3,0,8],[5,4,9,1]])

    print(data)

    return None

if __name__ == '__main__':
    var()
    # pca()
