#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from ctypes import *

# 加载动态链接库
lib = cdll.LoadLibrary('CDll.dll')

lib.hello()