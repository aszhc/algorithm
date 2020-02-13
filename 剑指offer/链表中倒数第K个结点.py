"""
输入一个链表，输出该链表中倒数第k个结点。
"""


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        Node = []
        while head is not None:
            Node.append(head)
            head = head.next
        if k > len(Node) or k < 1:
            return
        return Node[-k]

