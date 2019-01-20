#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

# 分类评估模型api
# sklearn.metrics.classification_report
from sklearn.metrics import classification_report




# alpha:拉普拉斯平滑系数


def naviebayes():
    """
    朴素贝叶斯进行文体分类
    :return:
    """
    news = fetch_20newsgroups(subset='all')

    # 进行数据分割
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25)

    # 对数据集进行特征抽取
    tf = TfidfVectorizer()

    # 以训练集中的词的列表进行每篇文章重要性统计['a','b','c','d']
    x_train = tf.fit_transform(x_train)

    x_test = tf.transform(x_test)

    # 进行朴素贝叶斯算法的预测
    mlt = MultinomialNB(alpha=1.0)

    print(x_train.toarray())

    print(x_train)

    mlt.fit(x_train,y_train)

    y_predict = mlt.predict(x_test)

    print("预测的文章类别为：",y_predict)

    # 得出准确率
    print("准确率为：",mlt.score(x_test,y_test))

    # 得出精确率与召回率
    print("每个类别的精确率和召回率：",classification_report(y_test,y_predict,target_names=news.target_names))
    return None


if __name__ == '__main__':
    naviebayes()