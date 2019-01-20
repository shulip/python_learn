#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from PIL import Image
from PIL import ImageFilter


filename1 = "ae.png"

im = Image.open(filename1)
def gassin(im):
    # Todo modify the number
    im1 = im.filter(ImageFilter.GaussianBlur(10))
    return im1

im.show()
im1.show()