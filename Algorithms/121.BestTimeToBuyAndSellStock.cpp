class Solution {
public:
    int maxProfit(vector<int> &prices) {
        if (prices.size() <= 1) {
            return 0;
        }
        int minimum = prices[0];
        int maximum = 0;
        for (int i=1; i < prices.size(); i++) {
            minimum = min(prices[i], minimum);
            maximum = max(prices[i] - minimum, maximum);
        }
        return maximum;
    }
};
