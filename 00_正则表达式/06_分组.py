#!/usr/bin/env python 
# -*- coding:utf-8 -*-


import re

print(re.match(r"(?P<xixi>wodema)(?P=xixi)","wodemawodema").group())