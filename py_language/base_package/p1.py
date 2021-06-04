# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/4
Last Modified: 2021/6/4
Description: 内置包练习
"""

# 题目:
# 输入日期，判断这一天是这一年的第几天?

import datetime


def day_of_year(date_time):
    date1 = datetime.datetime.strptime(date_time, "%Y-%m-%d")
    date2 = datetime.datetime(year=int(date1.year), month=1, day=1)

    return (date1 - date2).days + 1


if __name__ == '__main__':
    test_date1 = '2021-06-01'
    days = day_of_year(test_date1)
    print(days)
