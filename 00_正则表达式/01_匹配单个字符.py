#!/usr/bin/env python 
# -*- coding:utf-8 -*-


"""
.:除\n
[]:
\d(\D相反):数字
\w(\W相反):数字，字母
\s(\S相反):任何空格字符
"""
import re

movie = '速度与激情[1-57-9]'

print(re.match(movie,'速度与激情7').group())