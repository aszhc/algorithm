#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 圆圈中最后剩的数.py
# @Author: ZhouChuang
# @Datetime : 2020/2/20 下午4:55
# @Desc  :
"""
         0                  n=1
f(n,m)={
         [f(n-1,m)+m]%n     n>1
"""

# -*- coding:utf-8 -*-

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0:
            return -1
        s = 0
        for i in range(2, n + 1):
            s = (s + m) % i
        return s



