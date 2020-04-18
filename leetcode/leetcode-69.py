# encoding=utf8
"""
实现 int sqrt(int x) 函数。
使用二分法
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x:int
        :rtype: int
        """
        l = 0
        r = x + 1
        while l < r:
            mid = l + (r-l)//2
            if mid*mid > x:
                r = mid
            else:
                l = mid + 1
        return l-1


if __name__ == "__main__":
    Sol = Solution()
    end = Sol.mySqrt(9)
    print(end)
