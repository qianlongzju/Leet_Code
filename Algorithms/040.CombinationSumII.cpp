class Solution {
public:
    vector<vector<int> > combinationSum2(vector<int> &candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int> > result;
        vector<int> path;
        DFS(result, path, candidates, target, 0);
        return result;
    }
    void DFS(vector<vector<int> > &result, vector<int> path, 
            vector<int> &candidates, int target, int level) {
        if (target == 0) {
            result.push_back(path);
            return;
        }
        for (int i = level; i < candidates.size(); i++) {
            if (i != level && candidates[i] == candidates[i-1]) continue;
            if (candidates[i] > target) break;
            path.push_back(candidates[i]);
            DFS(result, path, candidates, target-candidates[i], i+1);
            path.pop_back();
        }
    }
    /*
    vector<vector<int> > combinationSum2(vector<int> &candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int> > result;
        set<vector<int> > result2;
        vector<int> path;
        DFS(result2, path, candidates, target, 0, 0);
        for (set<vector<int> >::iterator it=result2.begin(); it != result2.end(); it ++) {
            result.push_back(*it);
        }
        return result;
    }
    void DFS(set<vector<int> > &result, vector<int> path, 
            vector<int> &candidates, int target, int level, int sum) {
        if (sum == target) {
            result.insert(path);
            return;
        }
        if (sum > target) return;
        for (int i = level; i < candidates.size(); i++) {
            path.push_back(candidates[i]);
            DFS(result, path, candidates, target, i+1, sum + candidates[i]);
            path.pop_back();
        }
    }
    */
    /*
    vector<vector<int> > combinationSum2(vector<int> &candidates, int target) {
        vector<vector<int> > result;
        set<vector<int> > temp;
        sort(candidates.begin(), candidates.end());
        int index[target+2];
        index[0] = candidates.size();
        solve(target, candidates, index, 0, temp);
        for (set<vector<int> >::iterator it=temp.begin(); it != temp.end(); it ++) {
            result.push_back(*it);
        }
        return result;
    }
    
    void solve(int target, vector<int> &candidates, int index[], 
            int n, set<vector<int> > &result) {
        if (target < 0)
            return ;
        if (target == 0) {
            vector<int> v;
            for (int i = n; i >= 1; i--) {
                v.push_back(candidates[index[i]]);
            }
            result.insert(v);
        }
    
        for (int i = index[n]-1; i >= 0; i--) {
            index[n+1] = i;
            solve(target-candidates[i], candidates, index, n+1, result);
        }
    }
    */
    /*
    vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
        vector<vector<int> > result;
        sort(candidates.begin(), candidates.end());
        int index[target];
        index[0] = 0;
        solve(target, 0, candidates, index, 0, result);
        return result;
    }
    
    void solve(int target, int sum, vector<int> &candidates, int index[], 
            int n, vector<vector<int> > &result) {
        if (sum > target)
            return;
        if (sum == target) {
            vector<int> v;
            for (int i=1; i <= n; i++) {
                v.push_back(candidates[index[i]]);
            }
            result.push_back(v);
        }
    
        for (int i = index[n]; i < candidates.size(); i++) {
            index[n+1] = i;
            solve(target, sum + candidates[i], candidates, index, n+1, result);
        }
    }
    // for further thoughts on
    // http://leetcode.com/2010/09/print-all-combinations-of-number-as-sum.html
    vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
        vector<vector<int> > result;
        sort(candidates.begin(), candidates.end());
        int index[target];
        index[0] = -1;
        solve(target, 0, candidates, index, 0, result);
        return result;
    }
    
    void solve(int target, int sum, vector<int> &candidates, int index[], 
            int n, vector<vector<int> > &result) {
        if (sum > target)
            return;
        if (sum == target) {
            vector<int> v;
            for (int i=1; i <= n; i++) {
                v.push_back(candidates[index[i]]);
            }
            result.push_back(v);
        }
    
        for (int i = index[n]+1; i < candidates.size(); i++) {
            index[n+1] = i+1;
            solve(target, sum + candidates[i+1], candidates, index, n+1, result);
        }
    }
    */
};
