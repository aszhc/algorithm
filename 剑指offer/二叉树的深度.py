#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 二叉树的深度.py
# @Author: ZhouChuang
# @Datetime : 2020/2/21 下午10:49
# @Desc  :

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        count = max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1
        return count