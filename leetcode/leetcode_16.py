# encoding=utf8
"""
@Date: 2020-01-14 21:28:16
@LastEditTime : 2020-01-14 22:23:59
@FilePath: /leetcode/leetcode_16.py

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest

# 思路:
1. 排序数组
2. 定义双指针，左指针＝ｉ+ 1,　右指针＝len(nums) - 1,当左指针 < 右指针时，循环
3. 判断　get_nums - target 和　res - target　的取值，更新res
4. 移动指针
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3:  # 排除特殊情况
            return None
        nums.sort()
        res = float("inf")  # py用来表示正无穷
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:    # 去重，提高效率
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                get_nums = nums[i] + nums[left] + nums[right]
                if get_nums == target:
                    return target
                if abs(get_nums - target) < abs(res - target):  # 说明get_nums更靠近目标
                    res = get_nums  # 更新内容
                if get_nums - target < 0:
                    left += 1
                else:
                    right -= 1
        return res


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    Sol = Solution()
    end = Sol.threeSumClosest(nums, target)
    print(end)
