#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/18 11:28
# @Author : ZhouChuang
# @Site : 
# @File : 反转链表.py
# @Software: PyCharm

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leetcode.leetcode_2 import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 1. 指针法
        # 申请两个节点，pre和 cur，pre指向None
        pre = None
        cur = head
        while cur:
            # 记录当前节点的下一个节点
            tmp = cur.next
            # 然后将当前节点指向pre
            cur.next = pre
            # pre和cur节点都前进一位
            pre, cur = cur, tmp
        return pre

        # 2. 递归解法
        # 2.1 终止条件是当前节点或者下一个节点 == null
        # 2.2 在函数内部，改变节点的指向，也就是head的下一个节点指向head递归函数那句
        # 递归终止条件是当前为空，或者下一个节点为空
        if head is None or head.next is None:
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList(head.next)
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur
