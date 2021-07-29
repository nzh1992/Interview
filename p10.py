# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/10
Last Modified: 2021/6/10
Description: 
"""
# 问题：
# 统计一段字符串中, 字符出现的次数


def count_str(data):
    dict_str = {}
    for i in data:
        dict_str[i] = dict_str.get(i, 0) + 1

    return dict_str


def count_str2(data):
    from collections import Counter

    c = Counter(data).most_common()
    print(dict(c))


if __name__ == '__main__':
    data = "AAaaBBbbbcAC"
    count_str2(data)
