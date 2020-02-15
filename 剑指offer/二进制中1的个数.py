#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 二进制中1的个数.py
# @Author: ZhouChuang
# @Datetime : 2020/2/16 上午12:19
# @Desc  :

"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""


# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n - 1) & n
        return count
