#!/usr/bin/env python3
# *******************************************************
# -*- encoding: utf-8 -*-
# -*- Time    : 2022/07/12 14:20:16
# -*- Author  : Allen_Jol
# -*- File    : 生成包含大小写字母、数字和特殊字符的随机字符串
# *******************************************************


import random
from random import shuffle


# def shuffle_str():
#     s = '!@#$%&^=-+/<>_(),'
#     # 将字符串转换成列表
#     str_list = list(s)
#     # 调用random模块的shuffle函数打乱列表
#     shuffle(str_list)
#     # 将列表转字符串
#     return ''.join(str_list)


# print(shuffle_str())

def get_code():
    code_list = []
    special_str = '!@#$%&^=-+/<>_(),'

    for i in range(48, 57):  # ASCII表示的数字0-9 chr()方法将10进制的数字传化为对应的字符
        code_list.append(chr(i))  # 将迭代器追加到列表
    for i in range(65, 91):  # A-Z
        code_list.append(chr(i))
    for i in range(97, 123):  # a-z
        code_list.append(chr(i))

    str_list = list(special_str)
    # 调用random模块的shuffle函数打乱列表
    random.shuffle(str_list)
    # 列表转换成字符串
    # print(''.join(str_list))
    special_str_final = ''.join(str_list)
    # print(special_str_final)
    # print(random.choice('abcdefghijklm'))
    for i in range(len(special_str_final)):
        code_list.append(random.choice(special_str_final))
    # print('code list:', code_list)

    code = random.sample(code_list, 6)  # 用于截取列表的指定长度的随机数，返回的是列表
    code_num = ''.join(code)  # 将列表里的元素以指定的字符连接生成一个新的字符串

    return code_num


print(get_code())
