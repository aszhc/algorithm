#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 二叉树中和为某一值的路径.py
# @Author: ZhouChuang
# @Datetime : 2020/2/21 下午12:25
# @Desc  :
"""
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点
形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
"""


# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.root = None

    def add(self, elem):
        node = TreeNode(elem)
        """如果树是空的，则对根节点赋值"""
        if self.root is None:
            self.root = node
        else:
            queue = [self.root]  # 队列
            # 对已有的节点进行层次遍历
            while queue:
                # 弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.left is None:
                    cur.left = node
                    return
                else:
                    queue.append(cur.left)
                if cur.right is None:
                    cur.right = node
                    return
                else:
                    queue.append(cur.right)

    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        result = []
        if root is None:
            return result
        self.sums = expectNumber
        self.DFS(root, result, [root.val])
        return result

    # def binaryTreePaths(self, root):
    #     if root is None:
    #         return []
    #     result = []
    #     self.DFS(root, result, [root.val])
    #     return result

    def DFS(self, root, result, path):
        if root.left is None and root.right is None and sum(path) == self.sums:
            result.append(path)
        if root.left is not None:
            self.DFS(root.left, result, path + [root.left.val])
        if root.right is not None:
            self.DFS(root.right, result, path+[root.right.val])


if __name__ == "__main__":
    Sol = Solution()
    Sol.add(1)
    Sol.add(2)
    Sol.add(3)
    Sol.add(4)
    Sol.add(5)
    Sol.add(6)
    Sol.add(7)
    Sol.add(8)
    # ans = Sol.binaryTreePaths(Sol.root)
    ans = Sol.FindPath(Sol.root, 4)
    print(ans)
