#include "leetcode.h"
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector< pair<double,ii> > vdii;
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
using namespace std;
class Solution {
public:
    int largestRectangleArea(vector<int> &height) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if (height.size() < 1) {
            return 0;
        }
        stack<int> heights, indexes;
        heights.push(height[0]);
        indexes.push(0);
        int largestArea = height[0];
        int i = 1;
        while (i < height.size()) {
            if (height[i] > heights.top()) {
                heights.push(height[i]);
                indexes.push(i);
            } else if (height[i] < heights.top()) {
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
    vi v;
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
