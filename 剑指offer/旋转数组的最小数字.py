#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 旋转数组的最小数字.py
# @Author: ZhouChuang
# @Datetime : 2020/2/15 上午2:35
# @Desc  :
"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""
# -*- coding:utf-8 -*-


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        left = 0
        right = len(rotateArray) - 1
        while left < right:
            if rotateArray[left] < rotateArray[right]:
                return rotateArray[left]
            mid = (left + right) // 2
            if rotateArray[left] < rotateArray[mid]:
                left = mid + 1
            elif rotateArray[mid] < rotateArray[right]:
                right = mid
            else:
                left += 1
        return rotateArray[left]