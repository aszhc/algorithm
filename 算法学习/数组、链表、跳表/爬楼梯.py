#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/17 21:54
# @Author : ZhouChuang
# @Site : 
# @File : 爬楼梯.py
# @Software: PyCharm
import math

class Solution:
    def climbStairs(self, n: int) -> int:
        # 1. 斐波那契数列，递推
        if n <= 0:
            return 0
        res, last = 1, 1
        for _ in range(1, n):
            res, last = res + last, res
        return res
        # 2. 斐波那契公式
        sqrt_5 = math.sqrt(5)
        fib_n = math.pow((1+sqrt_5)/2, n+1) - math.pow((1-sqrt_5)/2, n+1)
        return int(fib_n/sqrt_5)


if __name__ == '__main__':
    Sol = Solution()
    ans = Sol.climbStairs(5)
    print(ans)