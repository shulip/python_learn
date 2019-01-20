#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import multiprocessing
import os,time


def copy_file(queue,file_name,old_folder_name,new_folder_name):
    """完成文件的复制"""
    # print("======>模拟copy文件：从 %s 到 %s 文件名是：%s" % (old_folder_name,new_folder_name,file_name))
    with open(old_folder_name+'/' + file_name,'rb') as f:
        content = f.read()
        with open(new_folder_name+'/' + file_name,'wb') as n_f:
            n_f.write(content)
    # 如果拷贝完文件，那么就向队列中写入一个消息
    queue.put(file_name)


def main():
    # 1.获取用户要copy的文件夹的名字
    old_folder_name = input("请输入要copy的文件夹的名字:")

    # 2.创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass
    # 3.获取文件夹中的所有的待copy的名字   listdir()
    file_names = os.listdir(old_folder_name)

    # 4.创建进程池
    po = multiprocessing.Pool(5)

    # 5.创建queue
    queue = multiprocessing.Manager().Queue()

    # 6.向进程池中添加拷贝文件的任务
    for file_name in file_names:
        po.apply_async(copy_file,args = (queue,file_name,old_folder_name,new_folder_name))

    po.close()
    # po.join()

    all_file_num = len(file_names) #测一下所有文件个数
    complete_num = 0
    while True:
        file_name_this = queue.get()
        # print("已拷贝完成：%s" % file_name_this)
        complete_num += 1
        print("\r拷贝的进度为：%.2f %%" % (complete_num/all_file_num)*100,end="")
        if complete_num>=all_file_num:
            break

if __name__ == '__main__':
    main()

