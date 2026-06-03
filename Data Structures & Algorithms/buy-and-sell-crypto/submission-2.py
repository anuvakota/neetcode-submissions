class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = 0
        b = 1
        maxprof = 0
        while b < len(prices):
            if prices[b] > prices[s]:
                profit = prices[b] - prices[s]
                maxprof = max(maxprof,profit)
            else:
                s = b
            b += 1
        return maxprof
            