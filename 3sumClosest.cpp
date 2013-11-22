#include "leetcode.h"
class Solution {
public:
    int threeSumClosest(vector<int> &num, int target) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        sort(num.begin(), num.end());
        int n = num.size();
        int lowestGap = INT_MAX;
        int closestSum = 0;
        for (int i = 0;i < n; i++) {
            int j = i + 1;
            int k = n - 1;
            while (j < k) {
                int sum_three = num[i] + num[j] + num[k];
                int gap = target - sum_three;
                if (gap < 0) {
                    gap = -gap;
                }
                if (gap < lowestGap) {
                    lowestGap = gap;
                    closestSum = sum_three;
                }
                if (sum_three < target) {
                    j++;
                } else if (sum_three > target) {
                    k--;
                } else {
                    j++;
                    k--;
                }
            }
        }
        return closestSum;
    }
};
int main() {
    Solution s;
    vector<int> v;
    v.push_back(-1);
    v.push_back(2);
    v.push_back(1);
    v.push_back(-4);
    cout << s.threeSumClosest(v, 1) << endl;
    return 0;
}

