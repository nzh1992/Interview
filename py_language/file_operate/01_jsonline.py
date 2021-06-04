# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/4
Last Modified: 2021/6/4
Description: 读取jsonline格式的文件
"""
import sys


# 01. 按行迭代(全部读取)
def get_lines(fp):
    with open(fp, 'rb') as f:
        lines = f.readlines()
        print(sys.getsizeof(lines))
        return lines


# 02. 按行迭代（按行读取）
def get_lines2(fp):
    with open(fp, 'rb') as f:
        for i in f:
            yield i


# 03. 指定行数迭代（按指定行数读取）
def get_lines3(fp, nrows=2):
    l = []
    with open(fp, 'r') as f:
        data = f.readlines(nrows)

    l.append(data)
    yield l


# 04. 使用第三方包, jsonlines
import jsonlines


def get_lines4(fp):
    with jsonlines.open(fp) as f:
        return f


if __name__ == '__main__':
    fp = r"/Users/niziheng/python_code/Interview/py_language/file_operate/test1.jsonl"
    for e in get_lines4(fp):
        print(e)
