class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans_map = dict()
        for i in range(0, len(nums)):  # 一边将列表中的数添加到字典中，一边判断两数之差是否存在于字典中
            temp = target - nums[i]
            if temp in ans_map:  # 判断步骤
                return [ans_map[temp], i]
            ans_map[nums[i]] = i  # 添加步骤（切记先判断再添加，以免key冲突）


if __name__ == '__main__':
    Sol = Solution()
    end = Sol.twoSum([2, 7, 11, 15], 9)
    print(end)
