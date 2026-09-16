class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lowest = prices[0];
        int bigdiff = 0;

        for (int i = 0; i < prices.size(); i++){
            int profit = prices[i] - lowest;
            bigdiff = max(profit,bigdiff);
            lowest = min(lowest, prices[i]);
        }

        return bigdiff;
        
    }
};
