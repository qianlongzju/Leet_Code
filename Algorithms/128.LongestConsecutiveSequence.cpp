class Solution {
public:
    int longestConsecutive(vector<int>& num) {
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
