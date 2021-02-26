#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 翻转单词顺序列.py
# @Author: ZhouChuang
# @Datetime : 2020/2/19 下午5:09
# @Desc  :

# -*- coding:utf-8 -*-


class Solution:
    def ReverseSentence(self, s):
        # write code here
        new = s.split(" ")
        new.reverse()
        return " ".join(new)


if __name__ == '__main__':
    Sol = Solution()
    ans = Sol.ReverseSentence("student. a am I")
    print(ans)
