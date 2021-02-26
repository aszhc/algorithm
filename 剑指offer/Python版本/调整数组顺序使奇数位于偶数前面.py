"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""


# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        j = []
        o = []
        array.sort()
        for i in array:
            if i % 2 == 0:
                o.append(i)
            else:
                j.append(i)
        return j + o


if __name__ == '__main__':
    array = [2, 6, 3, 1, 8, 7, 0]
    Sol = Solution()
    ans = Sol.reOrderArray(array)
    print(ans)
