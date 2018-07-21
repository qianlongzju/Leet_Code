#include "leetcode.h"
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
int main() {
    Solution s;
    vector<int> v;
    v.push_back(2);
    v.push_back(1);
    cout << s.maxProfit(v) << endl;
    return 0;
}
