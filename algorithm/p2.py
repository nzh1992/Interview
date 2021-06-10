# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/10
Last Modified: 2021/6/10
Description: 
"""
# 问题：
# 统计一个文本中单词频次最高的10个单词。


import re
from collections import Counter


def get_highest_frequency_words_top_10(fp):
    with open(fp) as f:
        c = Counter(re.sub(r"\W+", " ", f.read()).split())

        words_top_10 = c.most_common(10)

        return list(map(lambda c:c[0], Counter(re.sub(r"\W+", " ", f.read()).split()).most_common(10)))


if __name__ == '__main__':
    fp = r"/Users/niziheng/python_code/Interview/algorithm/words.txt"
    words_top_10 = get_highest_frequency_words_top_10(fp)
    print(words_top_10)
