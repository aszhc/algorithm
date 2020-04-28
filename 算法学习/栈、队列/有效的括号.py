#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/23 13:05
# @Author : Mr. Zhou Chuang
# @Site : 
# @File : 有效的括号.py
# @Software: PyCharm

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1


if __name__ == '__main__':
    Sol = Solution()
    ans = Sol.isValid("())[]{}")
    # ans = Sol.isValid("")
    print(ans)

