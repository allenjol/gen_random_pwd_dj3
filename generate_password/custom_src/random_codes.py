#!/usr/bin/env python3
# *******************************************
# -*- encoding: utf-8 -*-
# -*- Time    : 2022/07/12 12:20:31
# -*- Author  : Allen_Jol
# -*- File    : random_codes.py
# *******************************************

import random

# 随机字符串
# https://www.codeleading.com/article/31095276154/
# digit_list = []
# upper_list = []
# lower_list = []
# for i in range(48, 58):     # 0-9
#     digit_list.append(chr(i))
# for i in range(65, 91):     # A-Z
#     upper_list.append(chr(i))
# for j in range(97, 123):    # a-z
#     lower_list.append(chr(j))

# lower_code = random.sample(lower_list, 1)
# upper_code = random.sample(upper_list, 1)

# lower_code = random.sample(lower_list, 1)[0]
# upper_code = random.sample(upper_list, 1)[0]

# print(digit_list)
# print(upper_list)
# print(lower_list)

# print(lower_code)
# print(upper_code)

# print(lower_code[0], type(lower_code[0]))
# print(upper_code[0], type(upper_code[0]))


def get_code():
    code_list = []
    #   for i in range(10):   # 0~9
    for i in range(48, 57):  #ASCII表示的数字0-9 chr()方法将10进制的数字传化为对应的字符
        code_list.append(chr(i))  #将迭代器追加到列表
    for i in range(65, 91):  # A-Z
        code_list.append(chr(i))
    for i in range(97, 123):  # a-z
        code_list.append(chr(i))
    code = random.sample(code_list, 6)  #用于截取列表的指定长度的随机数，返回的是列表
    code_num = ''.join(code)  #将列表里的元素以指定的字符连接生成一个新的字符串
    return code_num


print(get_code())
