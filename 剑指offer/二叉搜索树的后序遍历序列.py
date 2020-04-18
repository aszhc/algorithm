#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 二叉搜索树的后序遍历序列.py
# @Author: ZhouChuang
# @Datetime : 2020/2/20 下午3:03
# @Desc  :

"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""


# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        root = sequence[-1]  # 根节点
        i = 0
        while i < len(sequence) - 1:
            if sequence[i] > root:
                break
            i += 1
        for j in range(i, len(sequence)-1):
            if sequence[j] < root:
                return False
        left = True
        right = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i:len(sequence)-1])
        return left and right


if __name__ == '__main__':
    sequence = [1, 3, 2, 5, 7, 6, 4]
    Sol = Solution()
    ans = Sol.VerifySquenceOfBST(sequence)
    print(ans)
