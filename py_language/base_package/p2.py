# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/4
Last Modified: 2021/6/4
Description: 
"""
import random


def random_list(l):
    random.shuffle(l)
    return l


if __name__ == '__main__':
    # 问题
    # 给定一个列表，打乱原列表的顺序
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    new_l = random_list(l)
    print(new_l)

    print(f"l id：{id(l)}, new_l id:{id(new_l)}")
