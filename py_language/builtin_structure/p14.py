# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/4
Last Modified: 2021/6/4
Description: 
"""
# 问题：
# 了解functools模块么？请介绍一下reduce的用法

# reduce函数将一个序列中，前一次调用的结果和sequence的下一个元素传递给function。
# recude函数共三个参数，function（自定义函数），sequence（序列），initial（初始值）
# initial默认值为0


from functools import reduce


if __name__ == '__main__':
    l = [1,2,3,4]
    total = reduce(lambda x, y: x+y, l, 0)
    print(total)
