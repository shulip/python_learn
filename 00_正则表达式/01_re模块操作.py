#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import re


ret = re.match(r"[hH]ello","hello world")

print(ret.group())