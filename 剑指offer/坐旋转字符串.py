#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 坐旋转字符串.py
# @Author: ZhouChuang
# @Datetime : 2020/2/19 下午9:23
# @Desc  :
"""
。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
"""
# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        return s[n:] + s[:n]


if __name__ == '__main__':
    s = "abcXYZdef"
    n = 3
    Sol = Solution()
    ans = Sol.LeftRotateString(s, n)
    print(ans)