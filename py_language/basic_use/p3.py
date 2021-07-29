# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/11
Last Modified: 2021/6/11
Description: 
"""
# import os

import objgraph


# 使用第三方库，objgraph查看对象引用情况
objgraph.show_most_common_types(limit=50)