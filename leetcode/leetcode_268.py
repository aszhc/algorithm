class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # if nums[-1] != len(nums):
        #     return len(nums)
        # elif nums[0] != 0:
        #     return 0
        # for i in range(1, len(nums)):
        #     expected_num = nums[i-1] + 1  # nums[i] - nums[i-1] = 1 如果不满足则说明缺失数字在其中
        #     if nums[i] != expected_num:
        #         return expected_num
        nums_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in nums_set:
                return number


if __name__ == '__main__':
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    Sol = Solution()
    end = Sol.missingNumber(nums)
    print(end)