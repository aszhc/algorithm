#!/usr/bin/python3


class Solution(object):
    def __init__(self):
        self.mincount = float("inf")

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        if not coins:
            return -1

        coins.sort(reverse=True)

        self.myChange(coins, amount, 0)

        return -1 if self.mincount == float("inf") else self.mincount

    def myChange(self, coins, amount, count):
        if amount == 0:
            self.mincount = min(self.mincount, count)
            return

        if not coins:
            return

        max = amount // coins[0]
        i = max
        while i >= 0 and i+count < self.mincount:
            rest = amount - (coins[0]*i)
            self.myChange(coins[1:], rest, count + i)
            i -= 1


if __name__ == "__main__":
    Sol = Solution()
    ans = Sol.coinChange([11, 9, 1], 18)
    print(ans)
