# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/11
Last Modified: 2021/6/11
Description: 
"""
# 问题：
# python中如何动态获取和设置对象的属性

class A:
    pass


if __name__ == '__main__':
    a = A()

    # 设置属性
    setattr(a, 'x', 11)

    # 获取属性
    print(getattr(a, 'x', 0))
