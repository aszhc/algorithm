#!/usr/bin/python3


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        list_one = []

        def backtrack(nums, list_one):
            if not nums:
                res.append(list_one[:])  # 切记 [:]
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue  # 避免重复。
                list_one.append(nums[i])
                backtrack(nums[:i] + nums[i+1:], list_one)
                list_one.pop()

        backtrack(nums, list_one)
        return res


if __name__ == "__main__":
    Sol = Solution()
    ans = Sol.permuteUnique([1, 1, 2])
    print(ans)
