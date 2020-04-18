#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/18 0:25
# @Author : ZhouChuang
# @Site : 
# @File : 盛最多水的容器.py
# @Software: PyCharm
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 1. 双指针法， 用max_area保存最大值
        left_point = 0
        right_point = len(height) - 1
        max_area = 0
        while left_point < right_point:
            area = min(height[right_point], height[left_point]) * (right_point - left_point)
            max_area = max(area, max_area)
            if height[left_point] < height[right_point]:
                left_point += 1
            else:
                right_point -= 1
        return max_area

        # l, r = 0, len(height) - 1
        # ans = 0
        # while l < r:
        #     ans = max(ans, min(height[r], height[l]) * (r - l))
        #     if height[l] < height[r]:
        #         l += 1
        #     else:
        #         r -= 1
        # return ans


if __name__ == '__main__':
    Sol = Solution()
    # ans = Sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    ans = Sol.maxArea([2, 3, 4, 5, 18, 17, 6])
    print(ans)
