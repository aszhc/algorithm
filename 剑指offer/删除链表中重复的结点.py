#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/6 下午7:34
# @Author : ZhouChuang
# @Site : 
# @File : 删除链表中重复的结点.py
# @Software: PyCharm

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        newhead = ListNode('a')
        newhead.next = pHead
        pre, cur = None, newhead
        while cur:
            pre = cur
            cur = cur.next
            # 判断指针的下一个值是否与当前值相等
            while cur and cur.next and cur.val == cur.next.val:
                t = cur.val
                # 和当前值t相等的结点都被抛弃
                while cur and t == cur.val:
                    cur = cur.next
                pre.next = cur
        return newhead.next
