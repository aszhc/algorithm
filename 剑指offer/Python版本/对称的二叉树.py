#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 对称的二叉树.py
# @Author: ZhouChuang
# @Datetime : 2020/2/21 下午11:28
# @Desc  :

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.compare(pRoot.left, pRoot.right)

    def compare(self, pRoot1, pRoot2):
        if not pRoot1 and not pRoot2:
            return True
        if not pRoot1 or not pRoot2:
            return False
        if pRoot1.val == pRoot2.val:
            if self.compare(pRoot1.left, pRoot2.right) and self.compare(pRoot1.right, pRoot2.left):
                return True
        return False
