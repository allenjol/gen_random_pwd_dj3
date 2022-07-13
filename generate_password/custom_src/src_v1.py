#!/usr/bin/env python3
# *******************************************
# -*- encoding: utf-8 -*-
# -*- Time    : 2022/07/11 13:15:36
# -*- Author  : Allen_Jol
# -*- File    : src.py
# *******************************************


import random
import string

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# a-z 的小写字母
alphabet = string.ascii_lowercase

# print(string.ascii_lowercase)
# print(string.ascii_uppercase)


def gen_rand_num_list():
    # 从字符串 alphabet 中随机选择两个小写字符用于替换最终的随机密码开头第一位和最后一位字母。
    # 这是因为我不想随机密码以特殊字符或者阿拉伯数字开头或者结尾
    rand_num_list = []
    for rand_num in range(2):
        rand_num_list.append(random.choice(alphabet))
    # print(f'rand_num_list: {rand_num_list}')

    return rand_num_list


# 定义生成简单密码接口
def gen_simple_interface():
    pw_length = 12
    upper_alphabet = alphabet.upper()
    # my_pw = ""
    pw_list = []

    # range(4) 即循环1次向列表中添加4个元素，循环4次一共添加12个元素
    for _ in range(pw_length // 3):
        pw_list.append(alphabet[random.randrange(len(alphabet))])
        pw_list.append(upper_alphabet[random.randrange(len(upper_alphabet))])
        pw_list.append(str(random.randrange(10)))

    # print(pw_list)
    random.shuffle(pw_list)
    pw_string = "".join(pw_list)

    pw_string_list = []
    for pw_item in pw_string:
        pw_string_list.append(pw_item)
    # print(pw_string_list)

    # 如果字符串的第一位不是小写英文字母，就用gen_rand_num_list()[0]来代替
    if pw_string_list[0] not in alphabet:
        pw_string_list[0] = gen_rand_num_list()[0]

    # 如果字符串的最后一位不是小写英文字母，就用gen_rand_num_list()[1]来代替
    if pw_string_list[-1] not in alphabet:
        pw_string_list[-1] = gen_rand_num_list()[1]

    pw_string = "".join(pw_string_list)
    print(pw_string)

    # 以下这个是纯字母的方法，太过于简单了
    # for _ in range(pw_length):
    #     next_index = random.randrange(len(alphabet))
    #     my_pw = my_pw + alphabet[next_index]

    return pw_string


# 定义生成复杂密码的接口
def gen_complex_interface():
    upper_alphabet = alphabet.upper()
    symbol = "!@#$%^<>_()"
    pw_length = 15
    pw_list = []

    # range(pw_length // 4) = 3，每循环一次，列表就被append四次，
    # 即列表里面就有4个元素，一共循环pw_length // 4次，也就是 15 // 4 就是3次
    # 所以列表中一共就是12个元素
    for _ in range(pw_length // 4):
        pw_list.append(alphabet[random.randrange(len(alphabet))])
        pw_list.append(upper_alphabet[random.randrange(len(upper_alphabet))])
        pw_list.append(str(random.randrange(10)))
        pw_list.append(symbol[random.randrange(len(symbol))])

    # range(pw_length - len(pw_list)) = 15 - 12 =3，即range(0, 3),也是循环3次
    for _ in range(pw_length - len(pw_list)):
        pw_list.append(alphabet[random.randrange(len(alphabet))])

    # print(f'pw_list: {pw_list}')
    random.shuffle(pw_list)
    pw_string = "".join(pw_list)
    # print(pw_string)

    pw_string_list = []
    for pw_item in pw_string:
        pw_string_list.append(pw_item)
    # print(pw_string_list)

    # 如果字符串的第一位不是小写英文字母，就用gen_rand_num_list()[0]来代替
    if pw_string_list[0] not in alphabet:
        pw_string_list[0] = gen_rand_num_list()[0]

    # 如果字符串的最后一位不是小写英文字母，就用gen_rand_num_list()[1]来代替
    if pw_string_list[-1] not in alphabet:
        pw_string_list[-1] = gen_rand_num_list()[1]

    pw_string = "".join(pw_string_list)
    print(pw_string)

    return pw_string


if __name__ == '__main__':
    # print(gen_rand_num_list())
    # print('-' * 50)
    gen_simple_interface()
    gen_complex_interface()
