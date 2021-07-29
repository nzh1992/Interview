# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/10
Last Modified: 2021/6/10
Description: 
"""
import dis


def first(l=[1]):
    l.append(1)
    print(l)


print(dis.dis(first))