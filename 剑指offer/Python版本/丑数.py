#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 丑数.py
# @Author: ZhouChuang
# @Datetime : 2020/2/18 下午7:37
# @Desc  :

# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        uglyList = [1]
        p2 = 0
        p3 = 0
        p5 = 0
        for i in range(index-1):
            newUgly = min(uglyList[p2]*2, uglyList[p3]*3, uglyList[p5]*5)
            uglyList.append(newUgly)
            if newUgly % 2 == 0:
                p2 += 1
            if newUgly % 3 == 0:
                p3 += 1
            if newUgly % 5 == 0:
                p5 += 1
        return uglyList


if __name__ == '__main__':
    Sol = Solution()
    ans = Sol.GetUglyNumber_Solution(13)
    print(ans)

