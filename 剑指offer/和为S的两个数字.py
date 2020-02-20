#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 和为S的两个数字.py
# @Author: ZhouChuang
# @Datetime : 2020/2/20 下午4:29
# @Desc  :
"""
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
"""


# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        low = 0
        high = len(array) - 1
        while low < high:
            temp = array[low] + array[high]
            if temp == tsum:
                return [array[low], array[high]]
            elif temp < tsum:
                low += 1
            else:
                high -= 1
        return []


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6]
    Sol = Solution()
    ans = Sol.FindNumbersWithSum(array, 5)
    print(ans)
