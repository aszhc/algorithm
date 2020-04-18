#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 二叉搜索树与双向链表.py
# @Author: ZhouChuang
# @Datetime : 2020/2/21 下午3:32
# @Desc  :


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.listHead = None
        self.listTail = None

    def Convert(self, pRootOfTree):
        if pRootOfTree is None:
            return
        self.Convert(pRootOfTree.left)
        if self.listHead is None:
            self.listHead = pRootOfTree
            self.listTail = pRootOfTree
        else:
            self.listTail.right = pRootOfTree
            pRootOfTree.left = self.listTail
            self.listTail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listHead