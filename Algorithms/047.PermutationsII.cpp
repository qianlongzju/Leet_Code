class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        vector<int> permutation;
        vector<bool> isVisited(nums.size(), false);
        DFS(result, permutation, nums, isVisited);
        return result;
    }
    void DFS(vector<vector<int>>& result, vector<int>& permutation, vector<int>& nums, vector<bool>& isVisited) {
        if (permutation.size() == nums.size()) {
            result.push_back(permutation);
            return;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (isVisited[i] == true) continue;
            if (i != 0 && nums[i] == nums[i-1] && isVisited[i] == isVisited[i-1]) continue;
            isVisited[i] = true;
            permutation.push_back(nums[i]);
            DFS(result, permutation, nums, isVisited);
            permutation.pop_back();
            isVisited[i] = false;
        }
    }
    /*
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> result;
        set<vector<int>> uniqueResult;
        vector<int> temp;
        if (nums.size() == 1) {
            temp.push_back(nums[0]);
            result.push_back(temp);
            return result;
        }
        vector<int> sub(nums.begin()+1, nums.end());
        vector<vector<int>> v = permuteUnique(sub);
        for (int i=0; i < v.size(); ++i) {
            for (int j=0; j <= v[i].size(); j++) {
                temp = v[i];
                temp.insert(temp.begin()+j, nums[0]);
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
