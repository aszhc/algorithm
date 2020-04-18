#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 深度优先遍历.py
# @Author: ZhouChuang
# @Datetime : 2020/2/21 下午12:33
# @Desc  :


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Solution:
    def binaryTreePath(self, root):
        if root is None:
            return []
        result = []
        self.DFS(root, result, [root.val])
        return result

    def DFS(self, root, result, path):
        if root.left is None and root.right is None:
            result.append(path)
        if root.left is not None:
            self.DFS(root.left, result, path + [root.left.val])
        if root.right is not None:
            self.DFS(root.right, result, path + [root.right.val])

    def binaryTreePaths2(self, root):
        if root is None:
            return []
        result = []
        stack = []
        stack.append((root, [root.val]))
        while stack:
            node, path = stack.pop()
            if node.left is None and node.right is None:
                result.append(path)
            if node.left is not None:
                stack.append((node.left, path + [node.left.val]))
            if node.right is not None:
                stack.append((node.right, path + [node.right.val]))
        return result
