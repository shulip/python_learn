#!/usr/bin/env python 
# -*- coding:utf-8 -*-

student = ['Tom',18,'male']
name,age,gender = student
print(name,age,gender)
print("*"*20)

num_list = [100,29,13,0]
first,*left_num_list,last = num_list
print(first,left_num_list,last)
print("*"*20)

student_2 = [['Tom',(98,96,100)],['Jack',(98,96,97)]]
for name,(first,second,third) in student_2:
    print(name,first,second,third)
print("*"*20)

student_3 ={
    'name':'Tom',
    'age':18,
}

for k,v in student_3.items():
    print(k,'--->',v)
