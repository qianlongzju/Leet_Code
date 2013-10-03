class Solution {
public:
    vector<vector<int> > generate(int numRows) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<vector<int> > result;
        if (numRows == 0) {
            return result;
        }
        vector<int> v;
        v.push_back(1);
        result.push_back(v);
        for (int i=2; i <= numRows; i++) {
            vector<int> v;
            v.push_back(1);
            for (int j=1; j < i-1; j++) {
                v.push_back(result[i-2][j-1] + result[i-2][j]);
            }
            v.push_back(1);
            result.push_back(v);
        }
        return result;
    }
};
