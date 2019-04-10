class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
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
            isVisited[i] = true;
            permutation.push_back(nums[i]);
            DFS(result, permutation, nums, isVisited);
            permutation.pop_back();
            isVisited[i] = false;
        }
    }
    /*
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        permute(nums, 0, result);
        return result;
    }
    void permute(vector<int>& nums, int index,
            vector<vector<int>>& result) {
        if (nums.size() == index) {
            result.push_back(nums);
            return;
        }
        for (int i=index; i < nums.size(); ++i) {
            int temp = nums[i];
            nums[i] = nums[index];
            nums[index] = temp;
            permute(nums, index+1, result);
            temp = nums[i];
            nums[i] = nums[index];
            nums[index] = temp;
        }
    }
    */
    /*
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> temp;
        if (nums.size() == 1) {
            temp.push_back(nums[0]);
            result.push_back(temp);
            return result;
        }
        vector<int> sub(nums.begin()+1, nums.end());
        vector<vector<int>> v = permute(sub);
        for (int i=0; i < v.size(); ++i) {
            for (int j=0; j < v[i].size(); j++) {
                temp.clear();
                temp = v[i];
                int tmp = temp[j];
                temp[j] = nums[0];
                temp.insert(temp.begin(), tmp);
                result.push_back(temp);
            }
            temp = v[i];
            temp.insert(temp.begin(), nums[0]);
            result.push_back(temp);
        }
        return result;
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> temp;
        if (nums.size() == 1) {
            temp.push_back(nums[0]);
            result.push_back(temp);
            return result;
        }
        vector<int> sub(nums.begin()+1, nums.end());
        vector<vector<int>> v = permute(sub);
        for (int i=0; i < v.size(); ++i) {
            for (int j=0; j <= v[i].size(); j++) {
                temp = v[i];
                temp.insert(temp.begin()+j, nums[0]);
                result.push_back(temp);
            }
        }
        return result;
    }
    */
};
