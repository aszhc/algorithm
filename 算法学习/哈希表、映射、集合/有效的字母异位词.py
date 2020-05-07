#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/7 22:48
# @Author : Mr. Zhou Chuang
# @Site : 
# @File : 有效的字母异位词.py
# @Software: PyCharm


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. 哈希 set
        if len(s) != len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True
        # 2. 哈希 dict
        if len(s) != len(t):
            return False
        dit = {}
        for i in s:
            if i in dit:
                dit[i] += 1
            else:
                dit[i] = 1
        for i in t:
            if i in dit:
                dit[i] -= 1
            else:
                return False
        for i in dit:
            if dit[i] != 0:
                return False
        return True
        # 3. python 特性
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    s = "ansgram"
    t = "nagaram"
    Sol = Solution()
    ans =Sol.isAnagram(s,t)
    print(ans)