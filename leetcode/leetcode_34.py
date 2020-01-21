class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break
        return [left_idx, right_idx]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    Sol = Solution()
    end = Sol.searchRange(nums, target)
    print(end)