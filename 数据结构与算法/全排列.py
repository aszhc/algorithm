#!/usr/bin/env python3


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        list_one = []

        def backtrack(nums, list_one):
            if not nums:
                res.append(list_one[:])
                return
            for i in range(len(nums)):
                list_one.append(nums[i])
                backtrack(nums[:i] + nums[i+1:], list_one)
                list_one.pop()
        backtrack(nums, list_one)
        return res


if __name__ == "__main__":
    Sol = Solution()
    ans = Sol.permute([1, 2, 3])
    print(ans)
