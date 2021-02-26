#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/6 下午7:49
# @Author : ZhouChuang
# @Site : 
# @File : 斐波那契数列.py
# @Software: PyCharm

class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 1 or n == 2:
            return 1
        else:
            return self.Fibonacci(n-1) + self.Fibonacci(n-2)


if __name__ == '__main__':
    Sol = Solution()
    ans = Sol.Fibonacci(4)
    print(ans)