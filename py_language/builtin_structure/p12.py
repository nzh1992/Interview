# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/4
Last Modified: 2021/6/4
Description: 
"""
# 问题：
# 全字母短句 PANGRAM 是包含所有英文字母的句子，比如："A QUICK BROWN FOX JUMPS OVER THE LAZY DOG"。
# 定义并实现一个方法 get_missing_letter，传入一个字符串采纳数，返回参数字符串编程一个 PANGRAM 中所确实的字符。
# 应该忽略传入字符串参数中的大小写，返回应该都是小写字符并按字母顺序排序（请忽略所有非ASCII字符）
import string


def get_missing_letter(s):
    s1 = set(string.ascii_lowercase)
    s2 = set(s.lower())

    result = "".join(sorted(s1 - s2))
    return result


if __name__ == '__main__':
    s1 = "A slow yellow fox crawls under the proactive dog"
    print(get_missing_letter(s1))

