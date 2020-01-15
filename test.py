# encoding=utf8
'''
@Author: your name
@Date: 2019-11-28 18:36:26
@LastEditTime : 2020-01-14 23:22:03
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/home/zhou/algorithm/test.py
'''
# encoding=utf8

# phone = {'2': ['a', 'b', 'c'],
#          '3': ['d', 'e', 'f'],
#          '4': ['g', 'h', 'i'],
#          '5': ['j', 'k', 'l'],
#          '6': ['m', 'n', 'o'],
#          '7': ['p', 'q', 'r', 's'],
#          '8': ['t', 'u', 'v'],
#          '9': ['w', 'x', 'y', 'z']}

# print(phone['2'[0]])

# n = int(input())
# # sum = 0
# # for i in range(n+1):  # 实际遍历到n
# #     sum += i
# # print(sum)
# print(sum(range(1, n+1)))
#
shabi = input()
nums = input().split()
nums = list(map(int, nums))
nums.sort()
for i in nums:
    print(i, end=" ")

