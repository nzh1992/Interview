# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/10
Last Modified: 2021/6/10
Description: 
"""
# 问题：
# 请写出一个函数，满足以下条件
# 1. 该元素是偶数
# 2. 该元素在原list中是在偶数的位置（index是偶数）


def filter_numbers(number_list):
    return [i for i in number_list if i % 2 == 0 and number_list.index(i) % 2 == 0]


if __name__ == '__main__':
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(filter_numbers(numbers))
