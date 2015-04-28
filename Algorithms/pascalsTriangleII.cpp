class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> result;
        if (rowIndex == 0) {
            result.push_back(1);
            return result;
        }
        result.push_back(1);
        result.push_back(1);
        for (int i=2; i <= rowIndex; i++) {
            vector<int> v(result);
            result.clear();
            result.push_back(1);
            for (int j=1; j < i; j++) {
                result.push_back(v[j-1]+v[j]);
            }
            result.push_back(1);
        }
        return result;
    }
};
