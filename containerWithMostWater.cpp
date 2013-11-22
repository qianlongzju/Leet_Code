#include "leetcode.h"
class Solution {
public:
    int maxArea(vector<int> &height) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int n = height.size();
        int maxArea = 0;
        int area=0, i=0, j=n-1;
        while (i < j) {
            if (height[i] < height[j]) {
                area = height[i] * (j-i);
                i++;
            } else {
                area = height[j] * (j-i);
                j--;
            }
            if (area > maxArea) {
                maxArea = area;
            }
        }
        return maxArea;
    }
};
int main() {
    Solution s;
    vi v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(1);
    cout << s.maxArea(v) << endl;
    return 0;
}

