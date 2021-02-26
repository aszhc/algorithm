#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 把字符串转换为整数.py
# @Author: ZhouChuang
# @Datetime : 2020/2/19 下午4:22
# @Desc  :

class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        flag = 0
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            s = s[1:]
            flag = 1
        try:
            s = int(s)
        except:
            return 0
        if flag == 1:
            s = -s
        if s > 2147483647 or s < -2147483648:
            return 0
        else:
            return s