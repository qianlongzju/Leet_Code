class Solution {
public:
    vector<vector<int>> subsets(vector<int>& S) {
        sort(S.begin(), S.end());
        vector<vector<int>> results;
        vector<int> current;
        subsetsHelper(results, current, S, 0);
        return results;
    }
    void subsetsHelper(vector<vector<int>>& result, vector<int>& current,
            vector<int>& S, int pos) {
        result.push_back(current);
        for (int i = pos; i < S.size(); i++) {
            current.push_back(S[i]);
            subsetsHelper(result, current, S, i+1);
            current.pop_back();
        }
    }
    /*
    vector<vector<int>> subsets(vector<int>& S) {
        sort(S.begin(), S.end());        
        int n = S.size();
        vector<vector<int>> result;
        for (int i=0; i < pow(2, n); i++) {
            vector<int> v;
            int j = i;
            int k = 0;
            while (j != 0) {
                if (j & 0x01) {
                    v.push_back(S[k]);
                }
                k ++;
                j >>= 1;
            }
            result.push_back(v);
        }
        return result;
    }
    */
};
