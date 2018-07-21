class Solution {
public:
    int maxProfit(vector<int> &prices) {
        if (prices.size() <= 1) return 0;
        int profit = 0;
        for (int i=1; i < prices.size(); i++)
            profit += max(0, prices[i] - prices[i-1]);
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

