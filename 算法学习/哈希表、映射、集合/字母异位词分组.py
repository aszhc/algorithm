#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/7 23:31
# @Author : Mr. Zhou Chuang
# @Site : 
# @File : 字母异位词分组.py
# @Software: PyCharm
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dic = {}
        for s in strs:
            keys = "".join(sorted(s))
            if keys not in dic:
                dic[keys] = [s]
            else:
                dic[keys].append(s)
        return list(dic.values())



if __name__ == '__main__':
    Sol = Solution()
    ans = Sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(ans)