#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Imputer
import jieba
import numpy as np
import time


def dictvec():
    """
    字典数据抽取
    :return:None
    """
    # 实例化
    dict = DictVectorizer(sparse=False)
    # dict = DictVectorizer()

    # 调用fit_transform
    data = dict.fit_transform([{'city': '北京', 'temperature': 100, 'height': 20},
                               {'city': '上海', 'temperature': 60, 'height': 10},
                               {'city': '深圳', 'temperature': 40, 'height': 30}])

    print(dict.get_feature_names())

    print(dict.inverse_transform(data))

    print(data)
    return None


def countvec():
    """
    对文本特征值化
    :return: None
    """
    cv = CountVectorizer()

    # data = cv.fit_transform(['what is this?',"Sorry I don't know know know"])
    data = cv.fit_transform(['我 喜欢 数据库', "我 用 python"])

    print(cv.get_feature_names())  # 统计文章中所有的词，重复只记做一次

    print(data.toarray())  # 对每篇文章，在词的列表中统计每个词出现的次数,单个字母不统计（一个英文字母不反应主题，没有分类依据）


def cutword():
    # 都为生成器
    con1 = jieba.cut("今天天气不是很暖和，冬天带来的寒意愈发明显，我喜欢冬天的雪，尤其是南方的湿雪，但不喜欢下雨，因为下雨天太tm冷了！")

    con2 = jieba.cut("我在听老师讲话，这句话真的是瞎jb写的")

    con3 = jieba.cut("指某事做到乐极点,可以指坏事做尽,做得太狠,也可指做的好。 要结合语境,看前一句或者后一句话。太绝了可以是太好了,太出色了,")

    # 转换成列表
    content1 = list(con1)
    content2 = list(con2)
    content3 = list(con3)

    # 把列表转换成字符串
    c1 = ' '.join(content1)
    c2 = ' '.join(content2)
    c3 = ' '.join(content3)
    return c1, c2, c3


def hanzivec():
    """
    汉字特征值化
    :return:None
    """
    # 得到特征的重要性
    c1, c2, c3 = cutword()

    print(c1, c2, c3)

    cv = CountVectorizer()

    data = cv.fit_transform([c1, c2, c3])

    print(cv.get_feature_names())

    print(data.toarray())


def tfidfvec():
    """
    中文特征值化
    :return:None
    """
    c1, c2, c3 = cutword()

    print(c1, c2, c3)

    tf = TfidfVectorizer()

    data = tf.fit_transform([c1, c2, c3])

    print(tf.get_feature_names())

    print(data.toarray())


"""数值数据处理"""


def mm():
    """
    归一化处理
    :return: None
    """
    # mm = MinMaxScaler()
    mm = MinMaxScaler(feature_range=(2, 3))  # range为归一化范围
    data = mm.fit_transform([[23, 45, 12, 90], [14, 53, 23, 53], [90, 78, 63, 29]])

    print(data)

    return None


def stand():
    """
    标准化缩放
    :return: None
    """
    std = StandardScaler()

    data = std.fit_transform([[23, 45, 12, 90], [14, 53, 23, 53], [90, 78, 63, 29]])

    print(data)
    return None


def im():
    """
    缺失值处理
    :return: None
    """
    # NaN,nan
    # axis=0为列，axis=1为行
    im = Imputer(missing_values='NaN', strategy='mean', axis=0)

    data = im.fit_transform([[1,2],[np.nan,3],[7,6]])

    print(data)

    return None

def main():
    # dictvec()
    # countvec()
    # hanzivec()
    # tfidfvec()
    # mm()
    stand()
    # im()


if __name__ == '__main__':
    main()
