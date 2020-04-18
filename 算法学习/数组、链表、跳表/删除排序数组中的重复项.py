#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/15 20:36
# @Author : ZhouChuang
# @Site : 
# @File : 删除排序数组中的重复项.py
# @Software: PyCharm
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 思路1. 快慢指针，i是慢指针，j为快指针。如果nums[i]=nums[j],增加j以跳过。如果nums[j]!=nums[i],将快指针处的值复制到i+1处，
        #       最后返回的数为i+1
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == '__main__':
    Sol = Solution()
    ans = Sol.removeDuplicates([1, 1, 2])
    print(ans)
