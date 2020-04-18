#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 数组中只出现一次的数字.py
# @Author: ZhouChuang
# @Datetime : 2020/2/15 上午1:22
# @Desc  :
"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        hashMap = {}
        for i in array:
            if str(i) in hashMap:
                hashMap[str(i)] += 1
            else:
                hashMap[str(i)] = 1
        res = []
        for k in hashMap.keys():
            if hashMap[k] == 1:
                res.append(int(k))
        return res