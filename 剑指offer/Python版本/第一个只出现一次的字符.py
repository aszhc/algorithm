#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第一个只出现一次的字符.py
# @Author: ZhouChuang
# @Datetime : 2020/2/19 下午12:25
# @Desc  :

"""
题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
如果没有则返回 -1（需要区分大小写）.
"""


# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # if not s:
        #     return -1
        # for i in range(len(s)):
        #     if s.count(s[i]) == 1:
        #         return i
        # return -1
        length = len(s)
        if length == 0:
            return -1
        dictChar = {}
        for i in range(length):
            if s[i] not in dictChar:
                dictChar[s[i]] = 1
            else:
                dictChar[s[i]] += 1
        for i in range(length):
            if dictChar[s[i]] == 1:
                return i
        return -1


if __name__ == '__main__':
    Sol = Solution()
    ans = Sol.FirstNotRepeatingChar("google")
    print(ans)

