#encoding=utf8
""" 
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray


for i in range(1,len(nums)):    
    nums[i] = nums[i] + max(nums[i-1],0)
return max(nums)
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max_sub_sum = nums[0]
        for num in nums:
            sum += num
            if sum > max_sub_sum:
                max_sub_sum = sum
            if sum < 0:
                sum = 0
        return max_sub_sum


if __name__ == "__main__":
    Sol = Solution()
    end = Sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(end)
