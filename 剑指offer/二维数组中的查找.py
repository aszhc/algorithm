#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/5 下午6:32
# @Author : ZhouChuang
# @Site : 
# @File : 二维数组中的查找.py
# @Software: PyCharm

"""
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每
一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
"""


# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if len(array) == 0 or len(array[0]) == 0:
            return 0
        for i in range(len(array)):
            if array[i][0] < target <= array[i][-1]:
                for j in range(len(array[i])):
                    if array[i][j] == target:
                        return True
        return False


if __name__ == '__main__':
    target = 7
    array = [
        [0, 1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6],
        [3, 4, 5, 6, 7],
    ]
    Sol = Solution()
    ans = Sol.Find(target, array)
    print(ans)
