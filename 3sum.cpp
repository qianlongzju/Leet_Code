#include "leetcode.h"
class Solution {
public:
    vector<vector<int> > threeSum(vector<int> &num) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<vector<int> > result;
        sort(num.begin(), num.end());
        set<vector<int> > triplets;
        vector<int> triplet(3);
        int n = num.size();
        for (int i = 0;i < n; i++) {
            int j = i + 1;
            int k = n - 1;
            while (j < k) {
                int sum_three = num[i] + num[j] + num[k];
                if (sum_three < 0) {
                    j++;
                } else if (sum_three > 0) {
                    k--;
                } else {
                    triplet[0] = num[i];
                    triplet[1] = num[j];
                    triplet[2] = num[k];
                    triplets.insert(triplet);
                    j++;
                    k--;
                }
            }
        }
        for (set<vector<int> >::iterator it=triplets.begin(); it!=triplets.end(); ++it)
                result.push_back(*it);
        return result;
    }
};
int main() {

    return 0;
}

