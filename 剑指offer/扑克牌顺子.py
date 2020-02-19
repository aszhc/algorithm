#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 扑克牌顺子.py
# @Author: ZhouChuang
# @Datetime : 2020/2/19 下午8:51
# @Desc  :
"""

"""
# 1. 除0外没有数字重复 2. max - min < 5
# -*- coding:utf-8 -*-


class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) == 0:
            return False
        while min(numbers) == 0:
            numbers.remove(0)
        if max(numbers) - min(numbers) <= 4 and len(numbers) == len(set(numbers)):
            return True
        else:
            return False


if __name__ == '__main__':
    numbers = []
    # numbers = [0, 0, 1, 2, 3]
    Sol = Solution()
    ans = Sol.IsContinuous(numbers)
    print(ans)