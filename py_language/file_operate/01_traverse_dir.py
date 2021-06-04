# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/4
Last Modified: 2021/6/4
Description: 
"""
# 问题
# 设计实现遍历目录与子目录，抓取.py文件

# 方法一
import os


def traverse_dir(dir, suffix):
    tmp_list = []

    for root, dirs, files in os.walk(dir):
        for file_name in files:
            name, suf = os.path.splitext(file_name)
            if suf == suffix:
               tmp_list.append(os.path.join(root, file_name))

    return tmp_list


# 方法二
def pick(fp, suffix):
    if fp.endswith(suffix):
        print(fp)


def traverse_dir2(dir, suffix):
    file_list = os.listdir(dir)

    for file in file_list:
        fp = os.path.join(dir, file)

        if os.path.isfile(fp):
            pick(fp, suffix)
        else:
            traverse_dir2(fp, suffix)


# 方法三
from glob import iglob


def traverse_dir3(dir, suffix):
    for fp in iglob(f"{dir}/**/*{suffix}", recursive=True):
        print(fp)


if __name__ == '__main__':
    # 比如找到py_language目录中所有的py文件
    dir = "/Users/niziheng/python_code/Interview/py_language"

    # 方法一：
    # py_file_list = traverse_dir(dir, '.py')
    # print(py_file_list)

    # 方法二：
    # traverse_dir2(dir, '.py')

    # 方法三：
    traverse_dir3(dir, '.py')
