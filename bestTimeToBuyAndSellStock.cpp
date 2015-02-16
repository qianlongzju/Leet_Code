#include "leetcode.h"
class Solution {
public:
    int maxProfit(vector<int> &prices) {
        int max = 0;
        if (prices.size() <= 1) {
            return 0;
        }
        int minimum = prices[0];
        for (int i=1; i < prices.size(); i++) {
            if (prices[i] < minimum) {
                minimum = prices[i];
            } 
            if (prices[i] - minimum > max) {
                max = prices[i] - minimum;
            }
        }
        return max;
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

