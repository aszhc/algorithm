#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 最小k个数.py
# @Author: ZhouChuang
# @Datetime : 2020/2/17 下午8:22
# @Desc  :z

"""
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""


# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        tinput.sort()
        if k > len(tinput) or tinput == []:
            return []
        return tinput[:k]


if __name__ == '__main__':
    tinput = [4, 5, 1, 6, 2, 7, 3, 8]
    Sol = Solution()
    ans = Sol.GetLeastNumbers_Solution(tinput, 3)
    print(ans)