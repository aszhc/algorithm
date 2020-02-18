#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 整数中1出现的次数.py
# @Author: ZhouChuang
# @Datetime : 2020/2/18 下午2:41
# @Desc  :

"""
题目描述
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,
但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
"""


# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(1, n + 1):
            tmp = i
            while tmp != 0:
                if tmp % 10 == 1:
                    count += 1
                tmp = tmp // 10
        return count


if __name__ == '__main__':
    Sol = Solution()
    ans = Sol.NumberOf1Between1AndN_Solution(13)
    print(ans)
