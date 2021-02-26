#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 数据流中的中位数.py
# @Author: ZhouChuang
# @Datetime : 2020/2/20 下午4:35
# @Desc  :

"""
使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
"""


# -*- coding:utf-8 -*-
class Solution:

    def __init__(self):
        self.data = []

    def Insert(self, num):
        # write code here
        self.data.append(num)
        self.data.sort()

    def GetMedian(self, data):
        # write code here
        length = len(self.data)
        if length % 2 == 0:
            return (self.data[length // 2] + self.data[length // 2 - 1]) / 2.0
        else:
            return self.data[int(length // 2)]
