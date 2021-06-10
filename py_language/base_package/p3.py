# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/10
Last Modified: 2021/6/10
Description: 
"""
# 问题
# 请描述如何使用re.sub方法
import re
from collections import Counter


s = "this is a good ((method for \\\\ check  \n file,  .....make sure the file correct."

a = re.sub(r"\W+", " ", s).split()

c = Counter(a)

top_10 = c.most_common(10)

print(dict(top_10))