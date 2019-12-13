#encoding=utf8
"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
在真实的面试中

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a_list = []
        for i in nums:
            if i not in a_list:
                a_list.append(i)
            else:
                a_list.remove(i)
        return a_list.pop()


if __name__ == "__main__":
    Sol = Solution()
    end = Sol.singleNumber([2,2,1])
    print(end)