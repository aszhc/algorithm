#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/15 0:15
# @Author : ZhouChuang
# @Site : 
# @File : 两数之和.py
# @Software: PyCharm
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. 遍历就完事了
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        """
        # 2. 哈希
        ans_map = dict()
        for i in range(len(nums)):
            want = target - nums[i]
            if want in ans_map:
                return [ans_map[want], i]
            ans_map[nums[i]] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    # nums = [3, 2, 4]
    target = 18
    Sol = Solution()
    ans = Sol.twoSum(nums, target)
    print(ans)

