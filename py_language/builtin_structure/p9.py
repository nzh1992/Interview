# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/4
Last Modified: 2021/6/4
Description: 
"""


# 问题：
# 请写出一段代码，实现删除list里面的重复元素


def rm_duplicate1(l):
    return list(set(l))


def rm_duplicate2(l):
    tmp_list = []
    [tmp_list.append(i) for i in l if i not in tmp_list]

    return tmp_list


def rm_duplicate3(l):
    tmp_list = sorted(set(l), key=l.index)
    return tmp_list


if __name__ == '__main__':
    l = [1, 1, 2, 3, 4, 4, 5]
    print(rm_duplicate3(l))
