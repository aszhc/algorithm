#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 剪绳子.py
# @Author: ZhouChuang
# @Datetime : 2020/2/18 下午5:14
# @Desc  :

class Solution:
    def cutRope(self, number):
        if number < 4:
            return number - 1
        a, b = number // 3, number % 3
        if b == 0:
            return pow(3, a)
        elif b == 1:
            return pow(3, a - 1) * 4
        else:
            return pow(3, a) * 2
