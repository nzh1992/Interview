# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/4
Last Modified: 2021/6/4
Description: 
"""
# 问题
# 给定两个列表，怎么找出他们相同的元素和不同的元素


l1 = [1, 2, 3]
l2 = [3, 4, 5]

s1 = set(l1)
s2 = set(l2)

# 相同元素
print(s1 & s2)

# 不同元素
print(s1 ^ s2)
