#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/20 20:22
# @Author : ZhouChuang
# @Site : 
# @File : 环形链表II.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        node = head
        while node:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return None
