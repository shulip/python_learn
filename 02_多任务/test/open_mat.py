#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scipy.io as sio


def array_in_mat(filename):
    # 获取参考图像和待配准图像图像信息
    data_1 = sio.loadmat(filename)
    img = data_1['imimg']
    return img
