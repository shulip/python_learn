#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from PIL import Image
from PIL import ImageFilter


im = Image.open("ae.png")
print(type(im))


# 图像增强
"""
out = im.filter(ImageFilter.DETAIL)
im.show()
out.show()
"""

# 点操作
# 应用点变换
"""
out2 = im.point(lambda i:i*1.2)     # 数值加大，亮度提高
out2.show()
"""

# 处理各个频段

im.show()
source = im.split()

R,G,B = 0,1,2

mask = source[R].point(lambda i:i<100 and 255)

out = source[G].point(lambda i:i*0.7)

source[G].paste(out,None,mask)

# 合并波段，build a new multiband image
im_out = Image.merge(im.mode,source)

im_out.show()