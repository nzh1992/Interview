# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/11
Last Modified: 2021/6/11
Description: 
"""
# 问题
# 遍历一个object的所有属性，并print每一个属性名


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_all_attributes(self):
        return [i for i in dir(self) if not i.startswith('__') and i != 'get_all_attributes']


if __name__ == '__main__':
    p = Person('jack', 28)
    print(p.get_all_attributes())
