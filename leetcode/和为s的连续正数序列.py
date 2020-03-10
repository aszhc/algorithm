#!/usr/bin/python


class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        left = 1
        right = 1
        res = []
        sum = 0

        while left <= target // 2:
            if sum < target:
                sum += right
                right += 1
            elif sum > target:
                sum -= left
                left += 1
            else:
                arr = list(range(left, right))
                res.append(arr)
                sum -= left
                left += 1
        return res


if __name__ == "__main__":
    Sol = Solution()
    ans = Sol.findContinuousSequence(9)
    print(ans)
