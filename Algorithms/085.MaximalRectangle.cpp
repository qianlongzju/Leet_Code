class Solution {
public:
    int maximalRectangle(vector<vector<char> > &matrix) {
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
