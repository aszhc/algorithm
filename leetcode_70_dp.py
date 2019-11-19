#encoding=utf8
""" 
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？ 

递归：
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n > 2:
            return self.climbStairs(n-1) + self.climbStairs(n-2)

"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        res,last = 1,1
        for _ in range(1,n):
            res,last = res+last,res
        return res

if __name__ == "__main__":
    Sol = Solution()
    ans = Sol.climbStairs(5)
    print(ans)