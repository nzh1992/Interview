# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/10
Last Modified: 2021/6/10
Description: 
"""


# 题目：
# 写一个函数，找出一个整数数组中第二大的数


def get_second_max(l):
    l.sort()
    return l[-2]


def get_second_max2(l):
    """
    利用两个标志位分别记录最大值和第二大值
    :param l:
    :return:
    """
    first_max = l[0]
    second_max = l[0]

    for i in l:
        if i > first_max:
            second_max = first_max
            first_max = i
        elif i > second_max:
            second_max = i

    return second_max


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7]
    second_max = get_second_max2(l)
    print(second_max)
