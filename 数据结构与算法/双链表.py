#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 双链表.py
# @Author: ZhouChuang
# @Datetime : 2020/2/16 下午6:41
# @Desc  :


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous

