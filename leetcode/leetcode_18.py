# encoding=utf8]
"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：
与三数之和类似：
先后固定其中两个数值 nums[a]、nums[b]，再使用双指针寻找与目标合适的差值
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        n = len(nums)
        for a in range(n - 3):
            # 防止重复
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            # 当最小值和都大于target， 跳出
            if nums[a] + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:
                break
            # 数组最大值和小于target, 就遍历下一个
            if nums[a] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue
            for b in range(a + 1, n - 2):
                # 防止重复
                if b - a > 1 and nums[b] == nums[b - 1]:
                    continue
                if nums[a] + nums[b] + nums[b + 1] + nums[b + 2] > target:
                    break
                if nums[a] + nums[b] + nums[n - 1] + nums[n - 2] < target:
                    continue
                # 双指针
                left = b + 1
                right = n - 1
                while left < right:
                    tmp = nums[a] + nums[b] + nums[left] + nums[right]
                    if tmp == target:
                        res.append([nums[a], nums[b], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif tmp > target:
                        right -= 1
                    else:
                        left += 1
        return res


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    Sol = Solution()
    end = Sol.fourSum(nums, target)
    print(end)