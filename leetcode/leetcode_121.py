# 121. 买卖股票的最佳时机
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # n = len(prices)
        # if n == 0:
        #     return 0
        #
        # # 初始化buying_prices, selling_prices
        # buying_prices = prices.copy()
        # selling_prices = prices.copy()
        #
        # # 计算每一天的最优买入价
        # buying_price = prices[0]
        # for i in range(n):
        #     if buying_price > prices[i]:
        #         buying_price = prices[i]
        #     buying_prices[i] = buying_price
        #
        # # 计算每一天可操作的最高卖出价
        # selling_price = prices[n-1]
        # for i in range(n-1, -1, -1):
        #     if selling_price < prices[i]:
        #         selling_price = prices[i]
        #     selling_prices[i] = selling_price
        #
        # max_profit = max([y - x for x, y in zip(buying_prices, selling_prices)])
        # return max(max_profit, 0)
        if len(prices) == 0:
            return 0
        max_profits = 0
        buying_price = prices[0]
        for i in range(len(prices)):
            if prices[i] < buying_price:
                buying_price = prices[i]
            else:
                profit = prices[i] - buying_price
                if profit > max_profits:
                    max_profits = profit
        return max_profits


if __name__ == '__main__':
    Sol = Solution()
    ans = Sol.maxProfit([7, 1, 5, 3, 6, 4])
    print(ans)
