#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from PIL import Image
import scipy.io as sio
import numpy as np
from matplotlib import pyplot as plt

def array_in_mat(filename):
    # 获取参考图像和待配准图像图像信息
    data_1 = sio.loadmat(filename)
    img = data_1['imimg']
    return img

def get_img(filename):
    data_1 = sio.loadmat(filename)
    arr = data_1['imimg']
    img = Image.fromarray(arr)
    return img

def show_mat_img(img):
    matrix = np.asarray(img)
    print(matrix)
    plt.imshow(matrix, cmap=plt.cm.bone)
    plt.show()


img = get_img("CT_1.mat")
show_mat_img(img)

"""
matrix = np.asarray(img)
print(matrix)
plt.imshow(matrix,cmap=plt.cm.bone)
plt.show()
"""