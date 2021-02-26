#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 二叉树的镜像.py
# @Author: ZhouChuang
# @Date  : 2020/2/15
# @Desc  :
"""
操作给定的二叉树，将其变换为源二叉树的镜像。
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root is None or (root.left is None and root.right is None):
            return root
        else:
            # 交换左右
            temp = root.left
            root.left = root.right
            root.right = temp
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)