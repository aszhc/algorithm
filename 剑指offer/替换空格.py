#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/5 下午6:43
# @Author : ZhouChuang
# @Site : 
# @File : 替换空格.py
# @Software: PyCharm
"""
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        return s.replace(" ", "%20")


if __name__ == '__main__':
    s = "we are happy"
    Sol = Solution()
    ans = Sol.replaceSpace(s)
    print(ans)
