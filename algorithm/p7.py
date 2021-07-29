# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/10
Last Modified: 2021/6/10
Description: 
"""
# 问题：
# 两个有序列表，l1和l2，对这两个列表进行合并，不可使用extend


def merge_list(l1, l2):
    [l1.append(i) for i in l2]
    return l1


if __name__ == '__main__':
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    l3 = merge_list(l1, l2)
    print(l3)
