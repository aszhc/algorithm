#encoding=utf8
'''''
给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。

示例 1:

输入: [1,4,3,2]

输出: 4
解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
提示:

n 是正整数,范围在 [1, 10000].
数组中的元素范围在 [-10000, 10000].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/array-partition-i
'''''
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = sorted(nums)
        num = 0
        for i in range(0, len(new_nums), 2):
            num += new_nums[i]
        return num
        # == return sum(sorted(nums)[::2])

if __name__ == "__main__":
    Sol = Solution()
    end = Sol.arrayPairSum([1,3,2,4])
    print(end)