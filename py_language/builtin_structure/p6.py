# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/4
Last Modified: 2021/6/4
Description: 
"""

# 问题：
# 预判下列语句的输出

l = [1, 2, 3]
print(l[10:])

# output: []
# 使用切片时需要注意，当索引越界时会返回一个空list，所以最佳实践是，在切片前判断一下list的长度，是否满足需求
