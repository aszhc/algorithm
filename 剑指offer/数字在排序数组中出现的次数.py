#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 数字在排序数组中出现的次数.py
# @Author: ZhouChuang
# @Datetime : 2020/2/15 上午1:18
# @Desc  :

"""
统计一个数字在排序数组中出现的次数。
"""
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        count = 0
        for i in range(len(data)):
            if data[i] == k:
                count += 1
        return count
