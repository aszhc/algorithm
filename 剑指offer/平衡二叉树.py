#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 平衡二叉树.py
# @Author: ZhouChuang
# @Datetime : 2020/2/21 下午10:53
# @Desc  :

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    res = True

    def IsBalanced_Solution(self, pRoot):
        # write code here
        self.helper(pRoot)
        return self.res

    def helper(self, root):
        if not root:
            return 0
        if not self.res:
            return 1
        left = 1 + self.helper(root.left)
        right = 1 + self.helper(root.right)
        if abs(left-right) > 1:
            self.res = False
        return max(left, right)
