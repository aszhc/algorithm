#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 顺时针打印矩阵.py
# @Author: ZhouChuang
# @Datetime : 2020/2/16 上午12:45
# @Desc  :
"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""

"""
1. 吸收第一行
2. 旋转矩阵 ：[[row[i] for row in matrix] for i in range(matrix[0] -1, -1, -1]
"""
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        res = []
        while 1:
            res.extend(matrix[0])
            if len(matrix) > 1:
                matrix = matrix[1::]
            else:
                break
            matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]) - 1, -1, -1)]  # 矩阵转置
        return res