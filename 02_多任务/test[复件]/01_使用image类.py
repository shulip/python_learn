#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from PIL import Image
# from __future__ import print_function
import os,sys

"""
# 尝试
a = sys.argv[0]
print(a)
b = sys.argv[0:]
print(b)
"""

filename1 = "ae.png"
filename2 = "CT_1.bmp.bmp"

# 打开图像
im = Image.open(filename2)
print(im.format,im.size,im.mode)        # 查看图像信息
# im.show()                             # 显示图像

"""
# 保存特定格式文件
infile = "ae.png"
f, e = os.path.splitext(infile)
outfile = f+'.jpg'
try:
    Image.open(filename1).save(outfile)
except:
    print("cannot convert", infile)
"""

# 识别图像文件
infile = "ae.png"
try:
    with Image.open(infile) as im:
        print(infile, im.format, "%dx%d" % im.size, im.mode)
except IOError:
    pass

"""
# 从图像复制子矩阵  要从图像中提取子矩形，请使用该crop()方法。
box = (100,100,400,400)     #（左，上，右，下）
im = Image.open("ae.png")
region = im.crop(box)
region.show()
"""

"""
# 处理子矩形并将其粘贴回去
box = (100,100,400,400)     #（左，上，右，下）
im = Image.open("ae.png")
region = im.crop(box)
region = region.transpose(Image.ROTATE_180)
im.paste(region,box)
im.show()
"""

"""
# 滚动图像
def roll(image,delta):
    # Roll an image sideways
    xsize,ysize = image.size

    delta = delta % xsize

    if delta == 0: return image

    part1 = image.crop((0,0,delta,ysize))
    part2 = image.crop((delta,0,xsize,ysize))
    image.paste(part1,(xsize-delta,0,xsize,ysize))
    image.paste(part2,(0,0,xsize-delta,ysize))

    return image

im = Image.open("ae.png")
im.show()
im2 = roll(im,200)
im2.show()
"""

"""
# 拆分和合并波段
im = Image.open("ae.png")
r,g,b = im.split()
im.show()
r.show()
g.show()
b.show()
im = Image.merge("RGB",(b,g,r))
im.show()
"""

# 几何变换
# 简单的几何变换
"""
im = Image.open("test.png")
# 改变大小
out1 = im.resize((128,128))
out1.show()
# 旋转
out2 = im.rotate(45)
out2.show()
# 转置图像
out3 = im.transpose(Image.FLIP_LEFT_RIGHT)
out3.show()
out4 = im.transpose(Image.FLIP_TOP_BOTTOM)
out4.show()
out5 = im.transpose(Image.ROTATE_90)
out5.show()
out6 = im.transpose(Image.ROTATE_180)
out6.show()
out7 = im.transpose(Image.ROTATE_270)
out7.show()
"""

# 颜色变换
"""
im = Image.open("ae.png").convert("L")
im.show()
"""

