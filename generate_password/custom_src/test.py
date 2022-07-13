#!/usr/bin/env python3
# *******************************************
# -*- encoding: utf-8 -*-
# -*- Time    : 2022/07/12 11:11:17
# -*- Author  : Allen_Jol
# -*- File    : Untitled-1
# *******************************************

import string
import secrets
# import random

symbol = "!@#$%&^=-+/<>_(),"


# 判断字符串是否属于特殊字符，其实是判断该字符是否为下划线
def assertStr(s):
    if s and (s in string.punctuation):
        return True
    else:
        return False


# 按照[a-zA-Z0-9_#]{6,16}的正则生成一个密码，其中小写、大写、数字分别为6位，下划线为2位
def genComplexPassword():
    password = ""
    char = string.ascii_letters + string.digits + symbol
    while True:
        password = ''.join(secrets.choice(char) for i in range(16))
        if (sum(c.islower() for c in password) == 4
                and sum(c.isupper() for c in password) == 4
                and sum(c.isdigit() for c in password) == 4
                and sum(assertStr(s) for s in password) == 4):
            break
    print(password)

    return password


# 按照[a-zA-Z0-9_#]{6,11}的正则生成一个密码，其中小写、大写、数字分别为3位，下划线为2位
def genSimplePassword():
    password = ""
    char = string.ascii_letters + string.digits + "_#"
    while True:
        password = ''.join(secrets.choice(char) for i in range(11))
        if (sum(c.islower() for c in password) == 3
                and sum(c.isupper() for c in password) == 3
                and sum(c.isdigit() for c in password) == 3
                and sum(assertStr(s) for s in password) == 2
                and password[0] != '_'
                and password[-1] != '_'
                and password[0] != '#'
                and password[-1] != '#'
                and '__' not in password
                and '##' not in password
                and '_#' not in password
                and '#_' not in password):
            break
    print(password)

    return password


if __name__ == "__main__":
    genSimplePassword()
    genComplexPassword()
