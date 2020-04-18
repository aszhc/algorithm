#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/14 18:39
# @Author : ZhouChuang
# @Site : 
# @File : 三数之和.py
# @Software: PyCharm
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                ans = nums[i] + nums[l] + nums[r]
                if ans < 0:
                    l += 1
                elif ans > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # break
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


if __name__ == '__main__':
    Sol = Solution()
    ans = Sol.threeSum([-1, 0, 1, 2, -1, -4])
    # ans = Sol.threeSum([0, 0, 0, 0])
    # ans = Sol.threeSum([-1, -1, 1, 1, 0])
    print(ans)
