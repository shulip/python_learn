#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from retrying import retry

@retry(stop_max_attempt_number=3)
def fun1():
    print("this is func 1")
    raise ValueError("this is test error")


fun1()