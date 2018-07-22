class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& num) {
        sort(num.begin(), num.end());
        vector<vector<int>> result;
        vector<int> permutation;
        vector<bool> isVisited(num.size(), false);
        DFS(result, permutation, num, isVisited);
        return result;
    }
    void DFS(vector<vector<int>>& result, vector<int>& permutation, vector<int>& num, vector<bool>& isVisited) {
        if (permutation.size() == num.size()) {
            result.push_back(permutation);
            return;
        }
        for (int i = 0; i < num.size(); i++) {
            if (isVisited[i] == true) continue;
            if (i != 0 && num[i] == num[i-1] && isVisited[i] == isVisited[i-1]) continue;
            isVisited[i] = true;
            permutation.push_back(num[i]);
            DFS(result, permutation, num, isVisited);
            permutation.pop_back();
            isVisited[i] = false;
        }
    }
    /*
    vector<vector<int>> permuteUnique(vector<int>& num) {
        vector<vector<int>> result;
        set<vector<int>> uniqueResult;
        vector<int> temp;
        if (num.size() == 1) {
            temp.push_back(num[0]);
            result.push_back(temp);
            return result;
        }
        vector<int> sub(num.begin()+1, num.end());
        vector<vector<int>> v = permuteUnique(sub);
        for (int i=0; i < v.size(); ++i) {
            for (int j=0; j <= v[i].size(); j++) {
                temp = v[i];
                temp.insert(temp.begin()+j, num[0]);
                uniqueResult.insert(temp);
            }
        }
        for (set<vector<int>>::iterator it=uniqueResult.begin(); it!=uniqueResult.end(); ++it) {
            result.push_back(*it);
        }
        return result;
    }
    */
};
