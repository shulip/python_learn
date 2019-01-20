#!/usr/bin/env python 
# -*- coding:utf-8 -*-

def test2(a, b, *args, **kwargs):
    print('--------------')
    print(a)
    print(b)
    print(args)
    print(kwargs)


def test1(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)
    # test2(a, b, args, kwargs)     # 相当于test2(1, 2, (3, 4, 5), {'name': 'haha', 'age': 10})
    # test2(a, b, *args, kwargs)    # 相当于test2(1, 2, 3, 4, 5, {'name': 'haha', 'age': 10})
    """此时*与**表示拆包"""
    test2(a, b, *args, **kwargs)    # 相当于test2(1, 2, 3, 4, 5, name='haha', age=10)


test1(1, 2, 3, 4, 5, name=['haha','we','re'], age=10)

# test1(1, 2, (3, 4, 5), {'name': 'haha', 'age': 10})
