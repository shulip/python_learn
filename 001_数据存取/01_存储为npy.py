#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import numpy as np

"""
np.save保存为npz格式，后面的参数为保存的数组名及内容，
形式为save_name=save_data,如果没有指定保存名字，就用arr_+str(i-1)，这个i是代表第几个要保存的数组；
如上所示：没有为第一个要保存的数组指定名字，其名字为'arr_0'，bg=b，bg为其名；np.load后内容为NpzFile类，取数据用字典加名字
"""


def save_2d_array():
    # array = np.arange(24).reshape((4, 6))
    array = np.random.randint(-1000,1000,(512,512,75))
    np.save("try_patient.npy", array)


def read_2d_array():
    b = np.load("2d_array.npy")
    print(b)


def save_3d_array():
    array = np.arange(24).reshape((2, 2, 6))

    np.save("3d_array.npy", array)


def read_3d_array():
    b = np.load("3d_array.npy")
    print(b)


def save_lots_array():
    """np.savez()函数输出的是一个扩展名为.npz的压缩文件，它包含多个与保存的数组对应的npy文件（由save()函数保存），文件名对应数组名"""
    a = np.arange(24).reshape((4, 6))
    b = np.arange(27).reshape((3, 3, 3))
    c = np.arange(27).reshape((3, 9))
    np.savez("with_3_array.npz", a, bg=b, img=c)


def read_lots_array():
    array = np.load("with_3_array.npz")
    print(array.keys())
    print(array['arr_0'])
    print(array['bg'])
    print(array['img'])


if __name__ == '__main__':
    # read_2d_array()
    # save_3d_array()
    # read_3d_array()
    # save_lots_array()
    read_lots_array()
    # save_2d_array()
