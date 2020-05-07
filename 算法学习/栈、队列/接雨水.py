#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/29 23:20
# @Author : Mr. Zhou Chuang
# @Site : 
# @File : 接雨水.py
# @Software: PyCharm
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 1. 暴力法
        # 能接多少雨水与左右两侧最近的比它高的有关
        # if not height:
        #     return 0
        # n = len(height)
        # max_left = [0] * n
        # max_right = [0] * n
        # max_left[0] = height[0]
        # max_right[-1] = height[-1]
        #
        # for i in range(1, n):
        #     max_left[i] = max(height[i], max_left[i-1])  # max_left处的值要么为本身，要么为前一个max_left
        # for i in range(n - 1 - 1, -1, -1):
        #     max_right[i] = max(height[i], max_right[i+1])
        # res = 0
        # for i in range(n):
        #     res += min(max_left[i], max_right[i])-height[i]
        #
        # return res

        # 2. 双指针
        # if not height:
        #     return 0
        # left = 0
        # right = len(height) - 1
        # res = 0
        # # 记录左右两边最大值
        # left_max = height[left]
        # right_max = height[right]
        # while left < right:
        #     if height[left] < height[right]:
        #         if left_max > height[left]:
        #             res += left_max - height[left]
        #         else:
        #             left_max = height[left]  # 更新 left_max
        #         left += 1
        #     else:
        #         if right_max > height[right]:
        #             res += right_max - height[right]
        #         else:
        #             right_max = height[right]  # 更新right_max
        #         right -= 1
        # return res

        length = len(height)
        if length < 3: return 0
        res, idx = 0, 0
        stack = []
        while idx < length:
            while len(stack) > 0 and height[idx] > height[stack[-1]]:
                top = stack.pop()  # index of the last element in the stack
                if len(stack) == 0:
                    break
                h = min(height[stack[-1]], height[idx]) - height[top]
                dist = idx - stack[-1] - 1
                res += (dist * h)
            stack.append(idx)
            idx += 1
        return res


if __name__ == '__main__':
    Sol = Solution()
    ans = Sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(ans)
