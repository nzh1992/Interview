# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/10
Last Modified: 2021/6/10
Description: 
"""
# 问题：
# 使用单一的列表生成式来产生一个新的列表
# 该列表至包含满足以下条件的值，元素为原始列表中的偶数切片
data = [1, 2, 5, 8, 10, 3, 18, 6, 20]

result = [i for i in data[::2] if i % 2 == 0]
print(result)
