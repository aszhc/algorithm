#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 包含min函数的栈.py
# @Author: ZhouChuang
# @Datetime : 2020/2/15 上午1:59
# @Desc  :
"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""
"""
链接：https://www.nowcoder.com/questionTerminal/4c776177d2c04c2494f2555c9fcc1e49?answerType=1&f=discussion
来源：牛客网

想调用min函数，我们需要有一个辅助栈，记录目前的最小值。
每次进行push操作，辅助栈中要压入当前数据栈中最小数字。
进行pop操作时，辅助栈弹出栈底数字。
进行min操作时，得到辅助栈栈底数字。

"""
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.data = []  # 数据栈
        self.assist = []  # 辅助栈

    def push(self, node):
        self.data.append(node)
        if len(self.assist) == 0 or node <= self.assist[-1]:
            self.assist.append(node)
        else:
            self.assist.append(self.assist[-1])

    def pop(self):
        if self.data:
            self.assist.pop()
            return self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def min(self):
        if self.assist:
            return self.assist[-1]
