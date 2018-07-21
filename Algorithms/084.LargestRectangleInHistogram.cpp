class Solution {
public:
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
int main() {
    Solution s;
    vector<int> v;
    v.push_back(2);
    v.push_back(1);
    v.push_back(5);
    v.push_back(6);
    v.push_back(2);
    v.push_back(3);
    cout << "right 10: " << s.largestRectangleArea(v) << endl;
    v.clear();
    v.push_back(1);
    v.push_back(1);
    cout << "right 2: " << s.largestRectangleArea(v) << endl;
    return 0;
}
