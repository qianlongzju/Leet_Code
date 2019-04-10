class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        vector<int> path;
        DFS(result, path, n, k, 1);
        return result;
    }
    void DFS(vector<vector<int>>& result,
            vector<int> path, 
            int n, int k, int min) {
        if (path.size() == k) {
            result.push_back(path);
            return;
        }
        for (int i = min; i <= n; i++) {
            path.push_back(i);
            DFS(result, path, n, k, i+1);
            path.pop_back();
        }
    }
    /*
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        vector<int> path;
        combine(result, path, n, k, 1);
        return result;
    }
    void combine(vector<vector<int>>& result,
            vector<int> path, 
            int n, int k, int min) {
        if (path.size() == k) {
            result.push_back(path);
            return;
        }
        if (min > n) {
            return;
        }
        combine(result, path, n, k, min+1);
        path.push_back(min);
        combine(result, path, n, k, min+1);
    }
    */
    /*
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        for (int i=0; i < pow(2, n); i++) {
            vector<int> v;
            int j = i;
            int p = 1;
            int q = 0;
            while (j != 0) {
                if (j & 0x01) {
                    v.push_back(p);
                    q ++;
                }
                p ++;
                j >>= 1;
            }
            if (k == q) {
                result.push_back(v);
            }
        }
        return result;
    }
    */
};
