# 接雨水

# 方法 1:
# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         if not height:
#             return 0
#         n = len(height)
#         max_left = [0] * n
#         max_right = [0] * n
#         max_left[0] = height[0]
#         max_right[-1] = height[-1]
#         # 找位置i左边最大值
#         for i in range(1, n):
#             max_left[i] = max(height[i], max_left[i-1])
#
#         for i in range(n-2, -1, -1):
#             max_right[i] = max(height[i], max_right[i+1])
#
#         res = 0
#         for i in range(n):
#             res += min(max_left[i], max_right[i]) - height[i]
#         return res


# 方法 2:
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        left = 0
        right = len(height) - 1
        res = 0
        # 记录左右两边最大值
        left_max = height[left]
        right_max = height[right]
        while left < right:
            if height[left] < height[right]:
                if left_max > height[left]:
                    res += left_max - height[left]
                else:
                    left_max = height[left]  # 更新 left_max
                left += 1
            else:
                if right_max > height[right]:
                    res += right_max - height[right]
                else:
                    right_max = height[right]  # 更新right_max
                right -= 1
        return res


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    Sol = Solution()
    end = Sol.trap(height)
    print(end)
