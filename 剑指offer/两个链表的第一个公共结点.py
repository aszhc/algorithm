#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 两个链表的第一个公共结点.py
# @Author: ZhouChuang
# @Datetime : 2020/2/28 下午11:45
# @Desc  :


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        a = pHead1
        b = pHead2
        while a != b:
            # a = a.next if a else pHead2
            # b = b.next if b else pHead1
            if a is None:
                a = pHead2
            else:
                a = a.next
            if b is None:
                b = pHead1
            else:
                b = b.next
        return a
