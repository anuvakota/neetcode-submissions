class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} #create the hashmap that stores ethe state that your in key = (i,buying) value = max_profit being made. i = day and second value is the state. 
        def dfs(i,buying):
            #base cases: if the value is zero there is nothing in the array or if its even equal to the the same amount or if the recurision has reached the end and theres no days left u cant buy
            if i >= len(prices):
                return 0 #bc u cant more anymore money
            if (i,buying) in dp: #if its already in the hashmap no need to recomputer
                return dp[(i,buying)] #return the max 

            #first decison : buy
            
            if buying:
                buy = dfs(i + 1, not buying) - prices[i] #I bought today, so tomorrow I own stock and therefore cannot buy again."
                cooldown = dfs(i + 1, buying)

                dp[(i,buying)] = max(buy,cooldown) 
            else: #u already have the stock: either sell or cooldown
                sell = dfs(i+2, not buying)  + prices[i]  #initially u cant buy so buy = false so now its not buy = true because u sold so ur ready to
                cooldown = dfs(i + 1, buying)
                dp[(i,buying)] = max(sell,cooldown) 

            return dfs(i,buying)
        return dfs(0,True) #initally true u have to buy
