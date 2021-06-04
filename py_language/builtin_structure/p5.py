# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/4
Last Modified: 2021/6/4
Description: 
"""
# 问题
# 按list中元素的age由大道小排序


l = [
    {'name': 'a', 'age': 20},
    {'name': 'b', 'age': 30},
    {'name': 'c', 'age': 40},
]

new_l = sorted(l, key=lambda x:x['age'], reverse=True)
print(new_l)

