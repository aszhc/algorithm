#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/20 20:22
# @Author : Zhou Chuang
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
        # 方法1: 哈希表
        visited = set()
        node = head
        while node:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return None

        # 方法2: Floyd算法（双指针两次相遇）
        fast, slow = head, head
        while True:
            if not (fast and fast.next):
                return
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
