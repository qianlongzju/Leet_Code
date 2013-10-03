#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<vector<int> > generateMatrix(int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<vector<int> > result;
        for (int i=0; i < n; i++) {
            vector<int> v;
            for (int j=0; j < n; j++) {
                v.push_back(0);
            }
            result.push_back(v);
        }
        int k=1;
        for (int i=0; i < n/2; i++) {
            int step = n-1-2*i;
            for (int j=0; j < step; j++) {
                result[i][i+j] = k++;
            }
            for (int j=0; j < step; j++) {
                result[i+j][n-1-i] = k++;
            }
            for (int j=0; j < step; j++) {
                result[n-1-i][n-1-(i+j)] = k++;
            }
            for (int j=0; j < step; j++) {
                result[n-1-(i+j)][i] = k++;
            }
        }
        if (n%2 == 1) {
            result[n/2][n/2] = k++;
        }
        return result;
    }
};
int main(){
    Solution s;
    int n = 3;
    vector<vector<int> > a = s.generateMatrix(n);
    for (int i=0; i < n; i++) {
        for (int j=0; j < n; j++) {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
