# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/4
Last Modified: 2021/6/4
Description: 
"""


# 问题：
# 将字符串"k:1 |k1:2|k2:3|k3:4"，处理成字典{k:1, k1:2, ...}


def str_to_dict(s):
    d = {}
    for iterms in s.split('|'):
        k, v = iterms.split(':')
        d[k] = v

    return d


def str_to_dict2(s):
    return {k: int(v) for items in s.split('|') for k, v in (items.split(':'),)}


if __name__ == '__main__':
    s = "k:1 |k1:2|k2:3|k3:4"
    result = str_to_dict2(s)
    print(result)
