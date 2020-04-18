#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/16 14:56
# @Author : ZhouChuang
# @Site : 
# @File : 旋转数组.py
# @Software: PyCharm
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. python 数组切片
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]

        # 2. 模拟插入
        while k != 0:
            nums.insert(0, nums.pop())
            k -= 1

        # 3. 三次翻转
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


if __name__ == '__main__':
    Sol = Solution()
    # ans = Sol.rotate([1, 2, 3, 4, 5, 6, 7], 3)
    ans = Sol.rotate([-1, -100, 3, 99], 2)
    print(ans)
