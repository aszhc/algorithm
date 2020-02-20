#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 字符串的排列.py
# @Author: ZhouChuang
# @Datetime : 2020/2/20 下午3:42
# @Desc  :
"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
"""

# -*- coding:utf-8 -*-


class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) <= 1:
            return ss
        res = set()  # 保证没有重复
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i]+ss[i+1:]):
                res.add(ss[i] + j)
        return sorted(res)


if __name__ == '__main__':
    Sol = Solution()
    ans = Sol.Permutation("abc")
    print(ans)
