# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/10
Last Modified: 2021/6/10
Description: 
"""
# 问题：
# 输入某年某月某日，判断这一天是这一年的第几天？


import datetime


input_date = "2021-01-31"

target_day = datetime.datetime.strptime(input_date, "%Y-%m-%d")
first_day = datetime.datetime(year=target_day.year, month=1, day=1)

day_count = target_day - first_day + datetime.timedelta(days=1)
print(day_count)
