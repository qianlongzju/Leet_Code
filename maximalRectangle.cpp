#include "leetcode.h"
class Solution {
public:
    int maximalRectangle(vector<vector<char> > &matrix) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int m = matrix.size();
        if (m == 0)
            return 0;
        int n = matrix[0].size();
        vector<vector<int> > heights(m, vector<int>(n, 0));
        for (int i=0; i < m; ++i) {
            for (int j=0; j < n; ++j) {
                if (matrix[i][j] == '0')
                    continue;
                if (i == 0)
                    heights[i][j] = 1;
                else 
                    heights[i][j] = heights[i-1][j] + 1;
            }
        }
        int maxArea = INT_MIN;
        for (int i=0; i < m; i++) {
            int area = largestRectangleArea(heights[i]);
            if (area > maxArea) 
                maxArea = area;
        }
        return maxArea;
    }
    int largestRectangleArea(vector<int> &height) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if (height.size() == 0) {
            return 0;
        }
        stack<int> heights, indexes;
        heights.push(height[0]);
        indexes.push(0);
        int largestArea = height[0];
        int i = 1;
        while (i < height.size()) {
            if (height[i] >= heights.top()) {
                heights.push(height[i]);
                indexes.push(i);
            } else {
                int h, j;
                while (!heights.empty() && height[i] < heights.top()) {
                    h = heights.top();
                    j = indexes.top();
                    int area = h * (i - j);
                    if (area > largestArea) {
                        largestArea = area;
                    }
                    heights.pop();
                    indexes.pop();
                }
                heights.push(height[i]);
                indexes.push(j);
            }
            i++;
        }
        while (!heights.empty()) {
            if (heights.top() * (i - indexes.top()) > largestArea) {
                largestArea = heights.top() * (i - indexes.top());
            }
            heights.pop();
            indexes.pop();
        }
        return largestArea;
    }
};
int main() {
    Solution s;
    vector<char> a;
    a.push_back('0');
    a.push_back('1');
    a.push_back('1');
    a.push_back('0');
    a.push_back('1');
    vector<char> b;
    b.push_back('1');
    b.push_back('1');
    b.push_back('0');
    b.push_back('1');
    b.push_back('0');
    vector<char> c;
    c.push_back('0');
    c.push_back('1');
    c.push_back('1');
    c.push_back('1');
    c.push_back('0');
    vector<char> d;
    d.push_back('1');
    d.push_back('1');
    d.push_back('1');
    d.push_back('1');
    d.push_back('0');
    vector<char> e;
    e.push_back('1');
    e.push_back('1');
    e.push_back('1');
    e.push_back('1');
    e.push_back('1');
    vector<char> f;
    f.push_back('0');
    f.push_back('0');
    f.push_back('0');
    f.push_back('0');
    f.push_back('0');
    vector<vector<char> > v;
    v.push_back(a);
    v.push_back(b);
    v.push_back(c);
    v.push_back(d);
    v.push_back(e);
    v.push_back(f);
    cout << s.maximalRectangle(v) << endl;

    return 0;
}

