class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) #stores how many steps total
        dp = [0] * (n+1) #create a array filled with 0s needs to be n+1 because +1 is the "top"
        #currently [0,0,0,0,0]
        for i in range (2, n + 1): # loops from 2 to n+1 and skip 0 and 1 because those are free starting points
            dp[i] = min(dp[i -1 ]+ cost[i -1], dp[i -2] + cost[i - 2])#the cost of what ur currently standing on plus the cost of moving up
        return dp[n] #returns whatever cost the least

        