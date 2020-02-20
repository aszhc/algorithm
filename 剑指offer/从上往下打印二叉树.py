#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 从上往下打印二叉树.py
# @Author: ZhouChuang
# @Datetime : 2020/2/20 下午2:39
# @Desc  :

"""
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        res = []
        newroot = [root]
        while newroot:
            nextlist = []  # 定义下一个列表, 每次循环都要清空
            for i in newroot:
                if i.left:
                    nextlist.append(i.left)
                if i.right:
                    nextlist.append(i.right)
                res.append(i.val)
            newroot = nextlist
        return res
