#!/usr/bin/env python 
# -*- coding:utf-8 -*-

"""
{}
*
+
?
"""
import re

re.match(r"速度与激情\d{1,2}", "速度与激情1").group()
re.match(r"速度与激情\d{1,2}", "速度与激情12").group()

print(re.match(r"\d{3,4}-?\d{11}", "02513851680442").group())
print(re.match(r"\d{3,4}-?\d{11}", "025-13851680442").group())

text = "asbd\nasda\nasdw\nwawda\n"

print(re.match(r".*", text).group())

# re.S允许.匹配\n
print(re.match(r".*", text, re.S).group())


