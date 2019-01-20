# !/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

"""转换器"""
# s = StandardScaler()
# print(s.fit_transform([[1,2,3],[4,5,6]]))
#
# ss = StandardScaler()
#
# print(ss.fit_transform([[1,2,3],[4,5,6]]))

"""估计器"""
"""
1、用于分类的估计器：
    sklearn.neighbors   k-近临算法
    sklearn.naive_bayes 贝叶斯算法
    sklearn.linear_model.LogisticRegression 逻辑回归
    sklearn.tree        决策树与随机森林
    
2、用于回归的分类器：
    sklearn.linear_model.LinearRegression   线性回归
    sklearn.linear_model.Ridge      岭回归
"""
"""
分类
特征值：x,y坐标，定位确定性，年月日时周       目标值：入住位置
处理：
1、由于数据量大，节约时间x、y缩小
2、时间戳进行（年，月，日，周，时分秒），当作新的特征
3、几千~几万，少于指定签到人数的位置删除
"""


def knncls():
    """
    K-近邻预测用户位置
    :return: None
    """
    # 窗口内输出不带省略号
    # pd.set_option('display.height', 1000)
    # pd.set_option('display.max_rows', 1000)
    # pd.set_option('display.max_columns', 1000)
    # pd.set_option('display.width', 1000)
    pd.set_option('display.width', 1000)  # 设置字符显示宽度
    pd.set_option('display.max_rows', 1000)  # 设置显示最大行
    pd.set_option('display.max_columns', None)  # 设置显示最大列

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

    x = data.drop(['place_id','row_id'], axis=1)  # 特征值


    # 进行数据的分割训练集合测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # print(data)
    # 特征化工程（标准化）
    std = StandardScaler()

    # 对测试集和训练集的特征值进行标准化
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)


    # 进行算法流程    # 超参数（n_neighbors）默认为5
    knn = KNeighborsClassifier(n_neighbors=8)

    # fit, predict,score
    knn.fit(x_train,y_train)

    # 得出预测结果
    y_predict = knn.predict(x_test)

    print("预测目标签到位置为：",y_predict)

    print("得出准确率：",knn.score(x_test,y_test))

    return None



if __name__ == '__main__':
    knncls()
