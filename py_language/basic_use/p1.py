# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/11
Last Modified: 2021/6/11
Description: 
"""
# 问题：
# 写一个类，并让他尽可能多的支持操作符


class Array:
    __list = []

    def __init__(self, l):
        self.__list = l
        print("构造函数")

    def __del__(self):
        print("析构函数")

    def __str__(self):
        print("描述函数")
        return str(self.__list)

    def __getitem__(self, item):
        return self.__list[item]

    def __len__(self):
        return len(self.__list)

    def add(self, value):
        self.__list.append(value)

    def remove(self, index):
        del self.__list[index]

    def display(self):
        print("All items:")
        for item in self.__list:
            print(item)


if __name__ == '__main__':
    a = Array([1,2,3,4,5,6])
    a.add(7)
    a.remove(0)

    print(a[0])
    print(a)

    # del a
