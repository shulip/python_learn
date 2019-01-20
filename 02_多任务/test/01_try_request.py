#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
import json

url = "https://www.baidu.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"}
response = requests.get(url,headers = headers,timeout = 3)


print("*"*30)
response.encoding = "utf-8"

print(response.text)

print("*"*30)

print(response.content.decode())

print("*"*30)

"""
html_str = response.content.decode()
dict_ret = json.loads(html_str)
print(dict_ret)
"""