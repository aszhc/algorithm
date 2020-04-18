#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/14 10:32
# @Author : ZhouChuang
# @Site : 
# @File : 移动零.py
# @Software: PyCharm
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 解法 1: 快慢指针
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j = j + 1

        # 解法2: python 内置函数
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)


if __name__ == '__main__':
    Sol = Solution()
    ans = Sol.moveZeroes([0, 1, 0, 3, 12])
    print(ans)

