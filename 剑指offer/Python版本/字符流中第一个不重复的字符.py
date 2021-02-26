#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 字符流中第一个不重复的字符.py
# @Author: ZhouChuang
# @Datetime : 2020/2/19 下午2:08
# @Desc  :
"""
题目描述
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
"""


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.s = ''
        self.dict = {}

    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.dict[i] == 1:
                return i
        return '#'

    def Insert(self, char):
        # write code here
        self.s = self.s + char
        if char in self.dict:
            self.dict[char] += 1
        else:
            self.dict[char] = 1
