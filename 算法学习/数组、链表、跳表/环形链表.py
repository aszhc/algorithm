#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/20 18:42
# @Author : ZhouChuang
# @Site : 
# @File : 环形链表.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 方法1: 哈希表
        # 从头遍历链表,将遍历到的元素放入字典里,如果有环的情况下那么必然会重复出现在哈希表;如果没有环,那么指针移动到最后就退出
        dic = {}
        while head:
            if head in dic:
                return True
            else:
                dic[head] = 1
            head = head.next
        return False

        # 方法2: 快慢指针追该碰撞
        if not head:
            return False
        slow = head
        quick = head
        while quick and slow:
            slow = slow.next
            if quick.next:  # quick跳两次，所以要判断quick.next是否为空
                quick = quick.next.next
            else:
                return False
            if quick is slow:
                return True
        return False
