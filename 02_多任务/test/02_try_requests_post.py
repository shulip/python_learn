#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
import json
url = "https://fanyi.baidu.com/basetrans"

query_str = input("输入需要翻译的中文：")

data ={"query": query_str,
       "from": "zh",
       "to": "en"}

headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
           "Referer":"https://fanyi.baidu.com/?aldtype=16047"}

response = requests.post(url,data=data,headers = headers)

# print("*"*30)
# print(response.content.decode())
# print(type(response.content.decode()))
# print("*"*30)

html_str = response.content.decode()
dict_ret = json.loads(html_str)
# print(dict_ret)
# print(type(dict_ret))
# print("*"*30)

ret = dict_ret['trans'][0]['dst']
print("翻译结果是：",ret)