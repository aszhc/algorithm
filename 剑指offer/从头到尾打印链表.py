#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/6 下午3:41
# @Author : ZhouChuang
# @Site : 
# @File : 从头到尾打印链表.py
# @Software: PyCharm
"""
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        res = []
        while listNode:
            res.append(listNode.val)
            listNode = listNode.next
        return res[::-1]

