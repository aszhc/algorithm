#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/28 20:59
# @Author : Mr. Zhou Chuang
# @Site : 
# @File : 滑动窗口最大值.py
# @Software: PyCharm
from typing import List
from collections import deque


class MonotonicQueue:
    def __init__(self):
        self.dq = deque([])

    def push(self, item):
        while self.dq and item > self.dq[-1]:
            self.dq.pop()

        self.dq.append(item)

    def pop(self, item):
        if item == self.dq[0]:
            self.dq.popleft()

    def max(self):
        return self.dq[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # # 1. 暴力模拟
        # res = []
        # for i in range(len(nums) - k + 1):
        #     res.append(max(nums[i:i + k]))
        # return res

        # 2. 双端队列
        if not nums or not k:
            return []

        monotonic_q = MonotonicQueue()

        for i in range(k - 1):
            monotonic_q.push(nums[i])

        result = []

        for i in range(k - 1, len(nums)):
            monotonic_q.push(nums[i])
            result.append(monotonic_q.max())
            monotonic_q.pop(nums[i - k + 1])

        return result


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    Sol = Solution()
    ans = Sol.maxSlidingWindow(nums, k)
    print(ans)
