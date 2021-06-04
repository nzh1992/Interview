# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/4
Last Modified: 2021/6/4
Description: 
"""


# 问题
# python遍历列表时，应该如何正确的删除元素?

# 核心思想：
# 遍历时，遍历的是新列表（浅拷贝或者深拷贝），删除的是原来的列表


# 方法一：利用切片的浅拷贝
def remove_from_list(l):
    for i in l[:]:
        if i < 5:
            pass
        else:
            l.remove(i)

    return l


# 方法二：利用filter函数生成新列表
def remove_from_list2(l):
    new_l = list(filter(lambda x: x < 5, l))
    print(id(l))
    print(id(new_l))  # id不同，是个新列表
    return new_l


# 方法三：列表解析
def remove_from_list3(l):
    new_l = [i for i in l if i < 5]
    print(id(l))
    print(id(new_l))  # id不同，是个新列表
    return new_l


# 方法四：倒序删除
# 因为遍历列表时一般是根据索引，从前向后遍历的，当元素被删除时，后面元素的索引发生了变化，从而引起的异常
# 所以我们可以根据索引倒序遍历列表，即使后面的元素被修改了，还没有被遍历的元素和索引还是保持不变的。
def remove_from_list4(l):
    for i in range(len(l)-1, -1, -1):
        if l[i] >= 5:
            l.remove(l[i])

    return l


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    print(remove_from_list4(l))
