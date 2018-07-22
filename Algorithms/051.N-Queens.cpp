class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<int> nums(n, 0);
        vector<vector<string>> result;
        solveNQueens(n, nums, result, 0);
        return result;
    }
    void solveNQueens(int n, vector<int>& nums, vector<vector<string>>& result, int level) {
        if (level == n) {
            result.push_back(getBoard(nums));
            return;
        }
        for (int j=1; j <= n; ++j) {
            nums[level] = j;
            if (isValid(nums, level))
                solveNQueens(n, nums, result, level+1);
        }
    }
    bool isValid(vector<int>& nums, int index) {
        for (int i=0; i < index; ++i) {
            if (nums[i] == nums[index])
                return false;
            if (abs(nums[i] - nums[index]) == (index - i))
                return false;
        }
        return true;
    }
    vector<string> getBoard(vector<int>& nums) {
        vector<string> board;
        for (int i=0; i < nums.size(); i++) {
            string s = "";
            for (int j=0; j < nums.size(); j++) {
                if (j+1 == nums[i]) {
                    s += "Q";
                } else {
                    s += ".";
                }
            }
            board.push_back(s);
        }
        return board;
    }
    /*
    vector<vector<string>> solveNQueens(int n) {
        vector<int> nums(n, 0);
        vector<vector<string>> result;
        solveNQueens(n, nums, result);
        return result;
    }
    void solveNQueens(int n, vector<int>& nums, vector<vector<string>>& result) {
        for (int i=0; i < n; ++i) {
            if (nums[i] != 0)
                continue;
            for (int j=1; j <= n; ++j) {
                nums[i] = j;
                if (isValid(nums, i))
                    solveNQueens(n, nums, result);
            }
            nums[i] = 0;
            return;
        }
        result.push_back(getBoard(nums));
    }
    bool isValid(vector<int>& nums, int index) {
        for (int i=0; i < index; ++i) {
            if (nums[i] == nums[index])
                return false;
            if (abs(nums[i] - nums[index]) == (index - i))
                return false;
        }
        return true;
    }
    vector<string> getBoard(vector<int>& nums) {
        vector<string> board;
        for (int i=0; i < nums.size(); i++) {
            string s = "";
            for (int j=0; j < nums.size(); j++) {
                if (j+1 == nums[i]) {
                    s += "Q";
                } else {
                    s += ".";
                }
            }
            board.push_back(s);
        }
        return board;
    }
    */
    /*
    // naive solution: tle
    vector<vector<string>> solveNQueens(int n) {
        vector<int> nums;
        for (int i = 0; i < n; i++) {
            nums.push_back(i);
        }
        vector<vector<string>> result;
        vector<vector<int>> permutations;
        permute(nums, 0, permutations);
        for (int i = 0; i < permutations.size(); i++) {
            if (isValid(permutations[i])) {
                result.push_back(getSolution(permutations[i]));
            }
        }
        return result;
    }
    bool isValid(vector<int> permutation) {
        for (int i=0; i < permutation.size(); i++) {
            for (int j=i+1; j < permutation.size(); j++) {
                if (j-i == permutation[j]-permutation[i]) {
                    return false;
                }
                if (j-i == permutation[i]-permutation[j]) {
                    return false;
                }
            }
        }
        return true;
    }
    vector<string> getSolution(vector<int> permutation) {
        vector<string> result;
        for (int i=0; i < permutation.size(); i++) {
            string s = "";
            for (int j=0; j < permutation.size(); j++) {
                if (j == permutation[i]) {
                    s += "Q";
                } else {
                    s += ".";
                }
            }
            result.push_back(s);
        }
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
};
