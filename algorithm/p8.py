# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/10
Last Modified: 2021/6/10
Description: 
"""
# 问题:
# 给定一个任意长度数组，实现一个函数
# 让所有技术都在偶数前面，而且奇数升序排列，偶数降序排列。
# 例如，字符串'1982376455',变成 '1355798642'


def special_sort(s):
    """
    最多只能使用一个列表
    :param s:
    :return:
    """
    if not isinstance(s, str):
        raise TypeError("s must be str type.")

    numbers = [int(i) for i in s]
    numbers.sort(reverse=True)

    for i in range(len(numbers)):
        if numbers[i] % 2 > 0:
            numbers.insert(0, numbers.pop(i))

    return "".join([str(i) for i in numbers])


def special_sort2(s):
    """
    允许使用多个列表
    :param s:
    :return:
    """
    if not isinstance(s, str):
        raise TypeError("s must be str type.")

    numbers = [int(i) for i in s]

    # 奇数列表
    l1 = []

    # 偶数列表
    l2 = []

    for i in numbers:
        if i % 2 == 0:
            l2.append(i)
        else:
            l1.append(i)

    # 奇数列表升序
    l1.sort()

    # 欧特殊列表降序
    l2.sort(reverse=True)

    l1.extend(l2)

    return "".join([str(i) for i in l1])


if __name__ == '__main__':
    s = '1982376455'
    a = special_sort2(s)
    print(a)
