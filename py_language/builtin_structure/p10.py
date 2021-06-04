# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/4
Last Modified: 2021/6/4
Description: 
"""
# 问题：
# 反转一个整数，例如 -123 -> -321
import sys


def reverse_int(s):
    if abs(s) < 10:
        return s

    str_s = str(s)

    if str_s[0] != '-':
        str_s = str_s[::-1]
        x = int(str_s)
    else:
        str_s = str_s[1:][::-1]
        x = -int(str_s)

    return x if abs(x) < sys.maxsize else 0


if __name__ == '__main__':
    s = -321
    print(reverse_int(s))
