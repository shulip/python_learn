#!/usr/bin/env python 
# -*- coding:utf-8 -*-

"""
match:从头匹配
search:从前向后搜索，满足一次后结束
findall:找到所有满足条件的值
sub:替换
split:切割
"""

import re

print(re.sub(r"\d+",'999','2313uhuhu2323hygu231231ihjih'))

def add(temp):
    strNum = temp.group()
    num = int(strNum)+1
    return str(num)

re.sub(r"\d+",add,'reee234') 。