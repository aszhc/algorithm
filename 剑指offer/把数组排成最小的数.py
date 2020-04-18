#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 把数组排成最小的数.py
# @Author: ZhouChuang
# @Datetime : 2020/2/18 下午3:50
# @Desc  :
"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""


# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        lenth = len(numbers)
        for i in range(0,lenth):  # 冒泡
            for j in range(i+1, lenth):
                if int(str(numbers[i])+str(numbers[j])) > int(str(numbers[j])+str(numbers[i])):
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        ans = ""
        for i in numbers:
            ans += str(i)
        return ans


if __name__ == '__main__':
    Sol = Solution()
    ans = Sol.PrintMinNumber([3, 32, 321])
    print(ans)