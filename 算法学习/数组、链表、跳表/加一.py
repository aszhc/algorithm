#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/17 12:26
# @Author : ZhouChuang
# @Site : 
# @File : 加一.py
# @Software: PyCharm
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits  # 处理 [9]这种特例


if __name__ == '__main__':
    Sol = Solution()
    ans = Sol.plusOne([9])
    print(ans)
