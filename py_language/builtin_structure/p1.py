# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/4
Last Modified: 2021/6/4
Description: 
"""
# 问题:
# 现有字典d= {'a':24,'g':52,'i':12,'k':33}，请按value进行排序


def sort_dict_by_value(d):
    new_d = sorted(d.items(), key=lambda x:x[1])
    return dict(new_d)


if __name__ == '__main__':
    d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
    new_d = sort_dict_by_value(d)

    print(new_d)