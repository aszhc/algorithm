#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 数组中出现次数超过一半 的数字.py
# @Author: ZhouChuang
# @Datetime : 2020/2/17 下午7:03
# @Desc  :

"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""


# -*- coding:utf-8 -*-
import collections


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # num = len(numbers) // 2
        # for number in numbers:
        #     count = 0
        #     for elem in numbers:
        #         if elem == number:
        #             count += 1
        #     if count > num:
        #         return number
        # return 0
        # sortedNum = sorted(numbers)
        # return sortedNum[len(numbers)//2]
        num = len(numbers) // 2
        dicts = {}
        for item in numbers:
            if item not in dicts:
                dicts[item] = 1
            else:
                dicts[item] += 1
        maxitem = max(dicts, key=dicts.get)
        if dicts[maxitem] > num:
            return maxitem
        else:
            return 0


if __name__ == '__main__':
    numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    Sol = Solution()
    ans = Sol.MoreThanHalfNum_Solution(numbers)
    print(ans)