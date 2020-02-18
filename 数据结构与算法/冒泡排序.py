#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 冒泡排序.py
# @Author: ZhouChuang
# @Datetime : 2020/2/18 下午3:37
# @Desc  :


def mp_sort(array):
    count = len(array)
    for i in range(0, count):
        for j in range(i+1, count):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
        print(array)


mp_sort([3, 1, 5, 9, 4])
