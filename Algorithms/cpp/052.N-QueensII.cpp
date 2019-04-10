class Solution {
public:
    int totalNQueens(int n) {
        int nums[n];
        memset(nums, 0, sizeof(nums));
        int result = 0;
        solveNQueens(0, n, nums, result);
        return result;
    }
    void solveNQueens(int index, int n, int *nums, int& result) {
        if (index == n) {
            result ++;
            return;
        }
        for (int j=1; j <= n; ++j) {
            nums[index] = j;
            if (isValid(nums, index))
                solveNQueens(index+1, n, nums, result);
        }
    }
    bool isValid(int *nums, int index) {
        for (int i=0; i < index; ++i) {
            if (nums[i] == nums[index] || abs(nums[i] - nums[index]) == abs(i - index))
                return false;
        }
        return true;
    }
    /*
    int totalNQueens(int n) {
        vector<int> nums;
        for (int i = 0; i < n; i++) {
            nums.push_back(i);
        }
        int result = 0;
        vector<vector<int>> permutations;
        permute(nums, 0, permutations);
        for (int i = 0; i < permutations.size(); i++) {
            if (isValid(permutations[i])) {
                result ++;
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
