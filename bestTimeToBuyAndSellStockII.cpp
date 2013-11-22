#include "leetcode.h"
class Solution {
public:
    int maxProfit(vector<int> &prices) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int profit = 0;
        if (prices.size() <= 1) {
            return 0;
        }
        for (int i=1; i < prices.size(); i++) {
            if (prices[i] > prices[i-1]) {
                profit += prices[i] - prices[i-1];
            } 
        }
        return profit;
    }
};
int main() {
    Solution s;
    vector<int> v;
    v.push_back(2);
    v.push_back(1);
    cout << s.maxProfit(v) << endl;
    return 0;
}

