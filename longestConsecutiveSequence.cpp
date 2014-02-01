#include "leetcode.h"
class Solution {
public:
    int longestConsecutive(vector<int> &num) {
        unordered_set<int> m;
        for (auto i: num)
            m.insert(i);
        int longestLength = 0;
        for (auto i: num) {
            int length = 1;
            for (int j=i+1; m.find(j) != m.end(); j++) {
                m.erase(j);
                length ++;
            }
            for (int j=i-1; m.find(j) != m.end(); j--) {
                m.erase(j);
                length ++;
            }
            longestLength = max(longestLength, length);
        }
        return longestLength;
    }
};
int main() {
    Solution s;
    vector<int> num;
    num.push_back(100);
    num.push_back(4);
    num.push_back(200);
    num.push_back(1);
    num.push_back(3);
    num.push_back(2);
    cout << s.longestConsecutive(num) << endl;
    return 0;
}
