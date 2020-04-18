# encoding=utf8
"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)

        def track_back(i, tmp):
            if(i == n):  # 越界
                return
            res.append(tmp)
            for j in range(i+1, n):
                track_back(j, tmp+[nums[j]])
        track_back(-1, [])
        return res


if __name__ == "__main__":
    Sol = Solution()
    end = Sol.subsets([1, 2, 3])
    print(end)
