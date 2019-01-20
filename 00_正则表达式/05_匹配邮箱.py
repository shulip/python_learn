#!/usr/bin/env python 
# -*- coding:utf-8 -*-


import re


def jiaoyan(e):
    email = "[\\w!#$%&'*+/=?^_`{|}~-]+(?:\\.[\\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\\w](?:[\\w-]*[\\w])?\\.)+[\\w](?:[\\w-]*[\\w])?$"
    ret = re.match(email,e)
    if ret:
        print(ret.group())
    else:
        print("邮箱格式错误")

jiaoyan("569159845@qq.com")
jiaoyan("we32323@live.comcomcom")
