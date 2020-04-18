#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 栈的压入、弹出序列.py
# @Author: ZhouChuang
# @Datetime : 2020/2/20 下午1:13
# @Desc  :
"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
"""


# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        while popV:
            # 如果stack的最后一个元素与popV中第一个元素相等，将两个元素都弹出
            if stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
            # 如果pushV中有数据，压入stack
            elif pushV:
                stack.append(pushV.pop(0))
            # 上面情况都不满足，直接返回false。
            else:
                return False
        return True


if __name__ == '__main__':
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 5, 3, 2, 1]
    Sol = Solution()
    ans = Sol.IsPopOrder(pushV, popV)
    print(ans)
    # print(pushV.pop())
