#include <string>
#include <algorithm>
#include <set>
#include <stack>
#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    vector<vector<int> > fourSum(vector<int> &num, int target) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<vector<int> > result;
        sort(num.begin(), num.end());
        set<vector<int> > quadplets;
        vector<int> quadplet(4);
        int n = num.size();
        //cout << n << endl;
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) { 
                int k = j + 1;
                int l = n - 1;
                while (k < l) {
                    int sum_four = num[i] + num[j] + num[k] + num[l];
                    if (sum_four < target) {
                        k++;
                    } else if (sum_four > target) {
                        l--;
                    } else {
                        quadplet[0] = num[i];
                        quadplet[1] = num[j];
                        quadplet[2] = num[k];
                        quadplet[3] = num[l];
                        //cout << quadplet[0] << " " << quadplet[1] << " " << quadplet[2] << " " << quadplet[3] << endl;
                        quadplets.insert(quadplet);
                        k++;
                        l--;
                    }
                }
            }
        }
        for (set<vector<int> >::iterator it=quadplets.begin(); it!=quadplets.end(); ++it)
                result.push_back(*it);
        return result;
    }
};
int main() {
    vector<int> a;
    a.push_back(2);
    a.push_back(1);
    a.push_back(0);
    a.push_back(-1);
    Solution s;
    vector<vector<int> > v = s.fourSum(a, 2);
    for (int i=0; i < v.size(); i++) {
        cout << v[i][0] << " " << v[i][1] << " " << v[i][2] << " " << v[i][3] << endl;
    }
    return 0;
}

