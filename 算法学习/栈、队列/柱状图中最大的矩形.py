#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/26 10:53
# @Author : Mr. Zhou Chuang
# @Site : 
# @File : 柱状图中最大的矩形.py
# @Software: PyCharm
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 1. 暴力破解
        res = 0
        n = len(heights)
        for i in range(n):
            left_i = i
            right_i = i
            while left_i >= 0 and heights[left_i] >= heights[i]:
                left_i -= 1
            while right_i < n and heights[right_i] >= heights[i]:
                right_i += 1
            res = max(res, (right_i - left_i - 1) * heights[i])
        return res
        # 2. 单调栈
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res


# if __name__ == '__main__':
#     heights = [2, 1, 5, 6, 2, 3]
#     Sol = Solution()
#     ans = Sol.largestRectangleArea(heights)
#     print(ans)


# 另一个解法
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        l = len(heights)
        if l == 0: return 0
        stack.append(0)
        maxare = heights[0]

        for i in range(1, l):
            while len(stack) > 1 and heights[i] < heights[stack[-1]]:
                s = heights[stack[-1]] * (i - stack[-2] - 1)
                maxare = max(maxare, s)
                # print(s, i, maxare)
                stack.pop()
            stack.append(i)

        # print('------')
        last = stack[-1]
        while len(stack) > 1:
            h = heights[stack.pop()]
            s = h * (last - stack[-1])
            maxare = max(maxare, s)
            # print(s, i, maxare)

        return maxare
