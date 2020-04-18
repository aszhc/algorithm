"""
@Author: ZhouChuang
@Date: 2020-01-31 13:15:18
@LastEditTime : 2020-01-31 16:25:37
@LastEditors  : Please set LastEditors
@Description: 动态规划
@FilePath: /undefined/home/zhou/algorithm/笔记/动态规划.py
"""


# 斐波那契数
class Solution1:  # 备忘录
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        self.cache = {0: 0, 1: 1}
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        if N in self.cache.keys():
            return self.cache[N]
        self.cache[N] = self.memoize(N - 1) + self.memoize(N - 2)
        return self.memoize(N)


class Solution2:  # 动态规划
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        a, b = 0, 1
        for _ in range(2, N + 1):
            a, b = b, a + b
        return b


# 凑零钱
class Solution3(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # if amount == 0:
        #     return 0
        # ans = float('inf')
        # for coin in coins:
        #     # 金额不可达
        #     if amount - coin < 0:
        #         continue
        #     subProb = self.coinChange(coins, amount - coin)
        #     # 子问题无解
        #     if subProb == -1:
        #         continue
        #     ans = min(ans, subProb + 1)
        # return ans if ans != float('inf') else -1

        # memo = {0: 0}
        #
        # def helper(n):
        #     if n in memo:
        #         return memo[n]
        #     res = float("inf")
        #     for coin in coins:
        #         if n >= coin:
        #             res = min(res, helper(n - coin) + 1)
        #     memo[n] = res
        #     return res
        #
        # return helper(amount) if (helper(amount) != float("inf")) else -1

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if (dp[-1] != float("inf")) else -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    Sol = Solution3()
    end = Sol.coinChange(coins, amount)
    print(end)
