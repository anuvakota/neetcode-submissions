class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = 0
        b = 1
        maxi = 0
        while b < len(prices):
            if prices[b] > prices[s]:
                profit = prices[b] - prices[s]
                maxi = max(maxi,profit)
            else:
                s = b
            b = b + 1
        return maxi