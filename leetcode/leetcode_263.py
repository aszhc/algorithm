#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : leetcode_263.py
# @Author: ZhouChuang
# @Datetime : 2020/2/18 下午7:38
# @Desc  :

class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        for e in [2, 3, 5]:
            while num % e == 0:
                num /= e
        return num == 1


if __name__ == '__main__':
    Sol = Solution()
    ans = Sol.isUgly(3)
    print(ans)