#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/6 下午5:59
# @Author : ZhouChuang
# @Site : 
# @File : leetcode_83.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
		:type head: ListNode
		:rtype: ListNode
		"""
        if not (head and head.next):
            return head
        i, j = head, head
        while j:
            if i.val != j.val:
                i = i.next
                i.val = j.val
            j = j.next
        i.next = None
        return head
