class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


if __name__ == '__main__':
    Sol = Solution()
    end = Sol.moveZeroes([0, 1, 0, 3, 12])
    print(end)
