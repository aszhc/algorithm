#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 连续子数组的最大和.py
# @Author: ZhouChuang
# @Datetime : 2020/2/18 下午2:08
# @Desc  :

"""

"""
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        dp = array
        for i in range(1, len(array)):
            dp[i] = max(dp[i-1]+array[i], array[i])
        return max(dp)


if __name__ == '__main__':
    ans = [6, -3, -2, 7, -15, 1, 2, 2]
    Sol = Solution()
    ans = Sol.FindGreatestSumOfSubArray(ans)
    print(ans)
