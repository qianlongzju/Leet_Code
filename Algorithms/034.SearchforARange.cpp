class Solution {
public:
    vector<int> searchRange(vector<int>& A, int target) {
        vector<int> v;
        if (A.size() == 0) {
            v.push_back(-1);
            v.push_back(-1);
            return v;
        }
        int n = A.size();
        int low = 0;
        int high = n-1;
        int middle;
        while (low <= high) {
            middle = low + (high-low)/2;
            if (A[middle] < target) {
                low = middle + 1;
            }
            else if (A[middle] > target) {
                high = middle - 1;
            }
            if (A[middle] == target) {
                break;
            }
        }
        if (A[middle] != target) {
            v.push_back(-1);
            v.push_back(-1);
            return v;
        }
        low = middle;
        while (low >= 0 && A[low] == target) {
            low --;
        }
        v.push_back(low+1);
        high = middle;
        while (high < n && A[high] == target) {
            high ++;
        }
        v.push_back(high-1);
        return v;
    }
};
