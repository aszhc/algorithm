#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/20 11:08
# @Author : ZhouChuang
# @Site : 
# @File : 两两交换链表中的节点.py
# @Software: PyCharm


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leetcode.leetcode_2 import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # # 方法一:递归
        # if not head or not head.next:
        #     return head
        #
        # first_node = head
        # second_node = head.next
        #
        # first_node.next = self.swapPairs(second_node.next)
        # second_node.next = first_node
        #
        # return second_node

        # 方法二:
        thead = ListNode(-1)
        thead.next = head
        c = thead
        while c.next or c.next.next:
            a, b = c.next, c.next.next
            c.next, a.next = b, b.next
            b.next = a
            c = c.next.next
        return thead.next


