class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> m;
        for (auto i: nums)
            m.insert(i);
        int longestLength = 0;
        for (auto i: nums) {
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
